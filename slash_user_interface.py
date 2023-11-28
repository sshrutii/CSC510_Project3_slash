"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: slash
"""

# Import Libraries
import sys
sys.path.append('../')
import streamlit as st
from streamlit import session_state
from src.main_streamlit import search_items_API
from src.url_shortener import shorten_url
import pandas as pd
import pymysql
import uuid
import base64
import csv
from io import BytesIO
import streamlit.components.v1 as components
#from link_button import link_button


# Adding DataTables CDN links to the head section
st.markdown(
    """
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.25/css/jquery.dataTables.min.css">
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.25/js/jquery.dataTables.min.js"></script>
    """,
    unsafe_allow_html=True
)

conn = pymysql.connect(host="localhost", user="root", password="mysql@123", db="slash")


def load_home_page(home):
    with home.container():
        cursor = conn.cursor()
        query = "SELECT history FROM user_history WHERE username=%s"
        values = (session_state.username)
        cursor.execute(query, values)
        record = cursor.fetchone()
        if record:
            record = record[0]

        # Hide Footer in Streamlit
        hide_menu_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
        st.markdown(hide_menu_style, unsafe_allow_html=True)

        st.success("Welcome {}".format(session_state.username))

        # Display Image
        st.image("assets/slash.png")

        st.write("Slash is a command line tool that scrapes the most popular e-commerce websites to get the best deals on the searched items across multiple websites. If a certain item is not found on the selected website, it will automatically show results from other websites.")
        product = st.text_input('Enter the product item name')
        website = st.selectbox('Select the website',('Costco', 'Walmart', 'Ebay', 'BestBuy', 'Target', 'Amazon', 'All'))

        website_dict = {
            'Amazon': 'az',
            'Walmart': 'wm',
            'Ebay': 'eb',
            'BestBuy': 'bb',
            'Target': 'tg',
            'Costco': 'cc',
            'All': 'all'
        }

        # Pass product and website to the method
        if st.button('Search') and product and website:
            results = search_items_API(website_dict[website], product)

            # If the result is not found on the selected website, search other websites
            if results is None:
                for key, value in website_dict.items():
                    if key == website:
                        continue
                    results = search_items_API(website_dict[key], product)
                    if results is not None:
                        break

            # Use st.columns based on return values
            if results is not None:
                items = []

                for result in results:
                    if result != {} and result['price'] != '':
                        print(result['price'])

                         # Clean up the price string
                        price_string = ''.join(result['price'].split())
                        price_string = ''.join(char for char in price_string if char.isdigit() or char == '.')

                         # Ensure there is a decimal point before the last two digits
                        if '.' not in price_string:
                            price_string = f'{price_string[:-2]}.{price_string[-2:]}'

                        # Check if the cleaned-up string is numeric
                        if price_string.replace('.', '').isdigit():
                            items.append(
                                {
                                    'Title': result['title'],
                                    'Price': float(price_string),
                                    'Website': result['website'],
                                    'Link': shorten_url(result['link'].split('\\')[-1])
                                }
                            )
                        else:
                            # Handle the case where the cleaned-up string is not numeric
                            items.append(
                                {
                                    'Title': result['title'],
                                    'Price': None,  # or any default value you prefer
                                    'Website': result['website'],
                                    'Link': shorten_url(result['link'].split('\\')[-1])
                                }
                            )

                csv = convert_df(pd.DataFrame(items))

                if len(items):
                    st.balloons()
                    #st.markdown("<h2 style='text-align: center; color: #1DC5A9;'>Search Results</h2>", unsafe_allow_html=True)

                    cheapest_item = None

                    for item in items:
                        if cheapest_item is None or item['Price'] < cheapest_item['Price']:
                            cheapest_item = item

                    items.remove(cheapest_item)
                    items.append(cheapest_item)

                    df = pd.DataFrame(items)
                    #st.table(df)
                    # Find the indexes of the cheapest and second cheapest items
                    cheapest_price = min(items, key=lambda x: x['Price'])['Price']
                    second_cheapest_price = sorted(set(item['Price'] for item in items))[1]

                    cheapest_indexes = [i for i, item in enumerate(items) if item['Price'] == cheapest_price]
                    second_cheapest_indexes = [i for i, item in enumerate(items) if item['Price'] == second_cheapest_price]

                    cheapest_item_1 = ""
                    cheapest_item_2 = ""
                    for i, item in enumerate(items):
                        if item['Price'] == cheapest_price:
                            cheapest_item_1 = f'{item["Title"]}//-//{item["Price"]}//-//{item["Link"]}'
                        elif item['Price'] == second_cheapest_price:
                            cheapest_item_2 = f'{item["Title"]}//-//{item["Price"]}//-//{item["Link"]}'

                    # Highlight the rows with the cheapest and second cheapest items
                    def highlight_cheapest(index):
                        background_color = 'background-color: lightgreen' if index in cheapest_indexes or index in second_cheapest_indexes else ''
                        return background_color

                    # Create an HTML table with custom styling
                    styled_table = '<table>'
                    sortedItems = sorted(items, key=lambda x: x['Price'])
                    count = 0

                    for i, item in enumerate(sortedItems):
                        style = 'background-color: lightgreen' if count < 2 else ''
                        row = f'<tr style="{style}">'
                        row += f'<td>{item["Title"]}</td>'

                       # Extract numerical part of the price and clean up the string
                        price_string = str(item['Price']).replace('$', '').replace(',', '')

                        # Check if the cleaned-up string is numeric
                        if price_string.replace('.', '').isdigit():
                            row += f'<td>{float(price_string)}</td>'
                        else:
                            row += '<td>Not Available</td>'  # or any default value you prefer

                        row += f'<td>{item["Website"]}</td>'
                        row += f'<td><a href="{item["Link"]}">Link to the product</a></td>'
                        row += '</tr>'
                        styled_table += row
                        count += 1
                    
                    try:
                        if record:
                            query = "UPDATE user_history SET history=%s WHERE username=%s"
                            values = (f'{record}, {cheapest_item_1}, {cheapest_item_2}', f'{session_state.username}')
                            cursor.execute(query, values)
                            conn.commit()
                        else:
                            query = "INSERT INTO user_history (username, history) VALUES (%s, %s)"
                            values = (f'{session_state.username}', f'{cheapest_item_1}, {cheapest_item_2}')
                            cursor.execute(query, values)
                            conn.commit()
                    except Exception as e:
                        pass

                    # Display the HTML table using DataTables
                    st.markdown("<h2 style='text-align: center; color: #1DC5A9;'>Search Results</h2>", unsafe_allow_html=True)

                    # Create an HTML table with DataTables options
                    styled_table = '<table id="results_table" class="display">'
                    styled_table += '<thead><tr>'
                    styled_table += '<th>Title</th>'
                    styled_table += '<th>Price</th>'
                    styled_table += '<th>Website</th>'
                    styled_table += '<th>Link</th>'
                    styled_table += '</tr></thead><tbody>'

                    count = 0
                    for i, item in enumerate(sortedItems):
                        style = 'background-color: lightgreen' if count < 2 else ''
                        row = f'<tr style="{style}">'
                        row += f'<td>{item["Title"]}</td>'
                        row += f'<td>{item["Price"]}</td>'
                        row += f'<td>{item["Website"]}</td>'
                        row += f'<td><a href="{item["Link"]}">Link to the product</a></td>'
                        row += '</tr>'
                        styled_table += row
                        count += 1

                    styled_table += '</tbody></table>'

                    # Display the DataTable
                    st.markdown(styled_table, unsafe_allow_html=True)

                    # DataTables initialization script
                    st.markdown(
                        """
                        <script>
                        $(document).ready(function() {
                            $('#results_table').DataTable({
                                "order": [[1, "asc"]],  // Sort by the second column (Price) in ascending order by default
                                "searching": true,      // Enable searching
                                "paging": true,         // Enable pagination
                                "lengthMenu": [10, 25, 50, 100],  // Display entries per page options
                                "pageLength": 10         // Default number of entries per page
                            });
                        });
                        </script>
                        """,
                        unsafe_allow_html=True
                    )

                    st.download_button(
                    label="Download data as CSV",
                    data=csv,
                    file_name='search_result.csv',
                    mime='text/csv',
                    )

                    
                    # pdf_button = st.button("Download PDF")

                    # if pdf_button:
                    #     # Convert the HTML table to PDF
                    #     pdf_data = html_to_pdf(styled_table)
                        
                    #     # Create a download link for the PDF
                    #     href = f'<a href="data:application/pdf;base64,{pdf_data}" download="search_results.pdf">Download PDF</a>'
                        
                    #     # Display the link (this can be done in a separate container or part of your layout)
                    #     st.markdown(href, unsafe_allow_html=True)    

        st.title("Search history")
        if record:
            recs = record.split(",")
            styled_table = '<table id="results_table" class="display">'
            styled_table += '<thead><tr>'
            styled_table += '<th>Title</th>'
            styled_table += '<th>Price</th>'
            styled_table += '<th>Link</th>'
            styled_table += '</tr></thead><tbody>'

            for r in recs:
                row = '<tr>'
                for val in r.split('//-//'):
                    row += f'<td>{val}</td>'
                row += '</tr>'
                styled_table += row      
            styled_table += '</tbody></table>'
            st.markdown(styled_table, unsafe_allow_html=True)
        else:
            st.write("No search history found")
            
# def html_to_pdf(html_code):
#     pdf_code = f'<html>{html_code}</html>'
#     pdf_b64 = components.html_to_pdf(pdf_code)
#     return pdf_b64

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def exit_home_page(home):
    home.empty()
    

def login(home):
    home.empty()
    login_holder = st.empty()
    with login_holder.container():
        st.title("Welcome")
        
        username = st.text_input("Username")
        password = st.text_input("Password",type='password')

        if st.button("Login"):
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE username=%s AND password=%s"
            values = (username, password)
            cursor.execute(query, values)
            record = cursor.fetchone()
            if record:
                session_state.login = True
                session_state.username = username
                st.success("Logged in as {}".format(username))
                login_holder.empty()
            else:
                st.warning("Incorrect username or password")

home = st.empty()

if 'login' not in session_state:
    session_state.login = False

if 'logoutpressed' not in session_state:
    session_state.logoutpressed = False

if not session_state.login:
    login(home)

if session_state.login:
    load_home_page(home)
    logoutContainer = st.empty()
    with logoutContainer.container():
        if st.button("Logout"):
            session_state.logoutpressed = True
            session_state.login = False
            session_state.username = None
            exit_home_page(home)
            loaded = False
            logoutContainer.empty()
            #login(home)

if session_state.logoutpressed:
    session_state.logoutpressed = False
    login(home)
    

# Add footer to UI
footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0%;
width: 100%;
background-color: #DFFFFA;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/anshulp2912/slash" target="_blank">slash</a></p>
<p><a style='display: block; text-align: center;' href="https://github.com/anshulp2912/slash/blob/main/LICENSE" target="_blank">MIT License Copyright (c) 2021 Rohan Shah</a></p>
<p>Contributors: Anshul, Bhavya, Darshan, Pragna, Rohan</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)