"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: slash
"""

# Import Libraries
import sys
sys.path.append('../')
import streamlit as st
from src.main_streamlit import search_items_API
from src.url_shortener import shorten_url
import pandas as pd
#from link_button import link_button


# Hide Footer in Streamlit
hide_menu_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)



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
                items.append(
                    {
                        'Title': result['title'],
                        'Price': float(''.join(result['price'].split('$')[-1].strip('$').rstrip('0').split(','))),
                        'Website': result['website'],
                        'Link': shorten_url(result['link'].split('\\')[-1])
                    }
                )

        if len(items):
            st.balloons()
            st.markdown("<h2 style='text-align: center; color: #1DC5A9;'>Search Results</h2>", unsafe_allow_html=True)

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

            # Highlight the rows with the cheapest and second cheapest items
            def highlight_cheapest(index):
                background_color = 'background-color: lightgreen' if index in cheapest_indexes or index in second_cheapest_indexes else ''
                return background_color

            # Create an HTML table with custom styling
            styled_table = '<table>'
            for i, item in enumerate(items):
                style = highlight_cheapest(i)
                row = f'<tr style="{style}">'
                row += f'<td>{item["Title"]}</td>'
                row += f'<td>{item["Price"]}</td>'
                row += f'<td>{item["Website"]}</td>'
                row += f'<td><a href="{item["Link"]}">Link to the product</a></td>'
                row += '</tr>'
                styled_table += row
            styled_table += '</table>'

            # Display the HTML table using st.markdown
            st.markdown(styled_table, unsafe_allow_html=True)



            st.markdown("<h2 style='text-align: center; color: #1DC5A9;'>Cheapest Item</h2>", unsafe_allow_html=True)
            st.write("Title:", cheapest_item['Title'])
            st.write("Price:", cheapest_item['Price'])
            st.write("Website:", cheapest_item['Website'])
            st.write("Link:", cheapest_item['Link'])


        else:
            st.error('No results found for the selected product and website.')


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
