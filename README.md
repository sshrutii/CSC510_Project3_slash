<p align="center"><img width="500" src="./assets/slash.png"></p>

<a href="https://zenodo.org/doi/10.5281/zenodo.10023583"><img src="https://zenodo.org/badge/703666512.svg" alt="DOI"></a>
[![codecov](https://codecov.io/gh/rohan22shah/slash-phase3/branch/main/graph/badge.svg?token=ZJ1AXQ5IFN)](https://codecov.io/gh/rohan22shah/slash-phase3)
[![Build Status](https://app.travis-ci.com/rohan22shah/slash-phase3.svg?branch=main)](https://app.travis-ci.com/rohan22shah/slash-phase3)
[![Python Style Checker](https://github.com/rohan22shah/slash-phase3/actions/workflows/style_checker.yml/badge.svg)](https://github.com/rohan22shah/slash-phase3/actions/workflows/style_checker.yml)
[![Run Tests On Push](https://github.com/abhi934/CSC510_Project2_slash-phase3/actions/workflows/unit_test.yml/badge.svg)](https://github.com/abhi934/CSC510_Project2_slash-phase3/actions/workflows/unit_test.yml)
[![Python Application](https://github.com/rohan22shah/slash-phase3/actions/workflows/python-app.yml/badge.svg)](https://github.com/rohan22shah/slash-phase3/actions/workflows/python-app.yml)
[![Lint Python](https://github.com/rohan22shah/slash-phase3/actions/workflows/main.yml/badge.svg)](https://github.com/rohan22shah/slash-phase3/actions/workflows/main.yml)
[![Running Code Coverage](https://github.com/rohan22shah/slash-phase3/actions/workflows/code_cov.yml/badge.svg)](https://github.com/rohan22shah/slash-phase3/actions/workflows/code_cov.yml)
[![Close as a feature](https://github.com/rohan22shah/slash-phase3/actions/workflows/close_as_a_feature.yml/badge.svg)](https://github.com/rohan22shah/slash-phase3/actions/workflows/close_as_a_feature.yml)

<!--Badges-->
<a href="https://github.com/rohan22shah/slash-phase3/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/rohan22shah/slash-phase3"></a>
<a href="https://github.com/abhi934/CSC510_Project2_slash-phase3/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/abhi934/CSC510_Project2_slash-phase3"></a>
<a href="https://github.com/abhi934/CSC510_Project2_slash-phase3/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/abhi934/CSC510_Project2_slash-phase3"></a>
<a href="https://github.com/abhi934/CSC510_Project2_slash-phase3/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/abhi934/CSC510_Project2_slash-phase3"></a>
<img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed/abhi934/CSC510_Project2_slash-phase3">
<img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/abhi934/CSC510_Project2_slash-phase3">



<p align="center">
    <a href="https://github.com/abhi934/CSC510_Project2_slash-phase3/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/abhi934/CSC510_Project2_slash-phase3/issues/new/choose">Request Feature</a>
</p>


Do you love shopping? Are you in search of some good deals while shopping online?! Slash is here to help you look for the best deals!


Slash is a publicly accessible web API framework that allows one to scrape the most popular e-commerce websites to get the best deals on the searched items across multiple e-commerce websites. Currently supported websites include [Amazon](https://www.amazon.com/), [Walmart](https://www.walmart.com/), [Target](https://www.target.com/), [BestBuy](https://www.bestbuy.com/), [Costco](https://www.costco.com/) and [EBay](https://www.ebay.com/).
- **Fast**: With slash, you can save over 50% of your time by comparing deals across websites within seconds
- **Easy**: Slash introduces easy to use public APIs to filter, sort and search through the search results
- **Powerful**: Produces JSON responses that can be easily customised to bring about the desired output
---

:movie_camera: Checkout our video
---

[![Slash Phase 3](https://yt-embed.herokuapp.com/embed?v=H1LSa4P-8fM)](https://www.youtube.com/watch?v=H1LSa4P-8fM "SLASH Phase 3")

---

:rocket: Installation
---
1. Clone the Github repository to a desired location on your computer. You will need [git](https://git-scm.com/) to be preinstalled on your machine. Once the repository is cloned, you will then ```cd``` into the local repository.
```
git clone https://github.com/rohan22shah/slash-phase3.git
cd slash
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those.
```
pip3 install -r requirements.txt
```
4. Once all the requirements are installed, you will have to ```cd``` into the ```src``` folder. Once in the ```src``` folder, use the python command to run the ```main.py``` file.
```
cd src

For Mac
python3 main.py

For Windows
python main.py
```
5. To run streamlit application
```
streamlit run slash_user_interface.py
```
Steps to install Chrome Extension:

1. Go to Extensions -> Enable Developer mode
2. Click on Load Unpacked
3. Select the pyscript-local-runtime folder from the repo
   
:Flutter
---
A new Flutter project.

Getting Started
This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

Lab: Write your first Flutter app
Cookbook: Useful Flutter samples
For help getting started with Flutter development, view the online documentation, which offers tutorials, samples, guidance on mobile development, and a full API reference.

### Requirements

- Flutter SDK installed
- Dart SDK
- Android Studio/IntelliJ/Visual Studio

:computer: Technology Used
---
- Streamlit [https://streamlit.io/]
- Android Studio
- Python
- Flutter
- Dart


:bulb: Use Case
---
* ***Students***: Students coming to university are generally on a budget and time constraint and generally spend hours wasting time to search for products on Websites. Slash is the perfect tool for these students that slashes all the unnecessary details on a website and helps them get prices for a product across multiple websites.Make the most of this tool in the upcoming Black Friday Sale.
* ***Data Analysts***: Finding data for any project is one of the most tedious job for a data analyst, and the datasets found might not be the most recent one. Using slash, they can create their own dataset in real time and format it as per their needs so that they can focus on what is actually inportant.

:page_facing_up: Why
---
- In a market where we are spoilt for choices, we often look for the best deals.  
- The ubiquity of internet access has leveled the retail playing field, making it easy for individuals and businesses to sell products without geographic limitation. In 2020, U.S. e-commerce sales, receiving a boost due to the COVID-19 pandemic, grew 44% and represented more than 21% of total retail sales, according to e-commerce information source Internet Retailer.
- The growth of e-commerce has not only changed the way customers shop, but also their expectations of how brands approach customer service, personalize communications, and provide customers choices.
- E-commerce market has prompted cut throat competition amongst dealers, which is discernable through the price patterns for products of major market players. Price cuts are somewhat of a norm now and getting the best deal for your money can sometimes be a hassle (even while online shopping).
- This is what Slash aims to reduce by giving you an easy to use, all in one place solution for finding the best deals for your products that major market dealers have to offer!
- Slash in its current form is for students who wish to get the best deals out of every e-commerce site and can be used by anyone who is willing to develop an application that consumes these web APIs.
- Future scope includes anything from a web application with a frontend or any Android or IOS application that utilises these Web APIs at their backend. Anyone can build their own custom application on top of these web APIs.

:golf: New Features added
---
- Login session Added
- Improved User Interface of Extention
- Added history of products searched
- Mobile App fixed in Flutter
- Flutter UI improvised significantly
- Fixed website search
- Download the complete list of searched products in a CSV format

## Flutter Features
- Search for products across multiple e-commerce websites (Amazon, Walmart, Target, BestBuy, Costco, eBay).
- Compare prices and deals to find the best offer.
- Easy-to-use interface for quick navigation and search.
- Redirect to the respective app/website


:golf: Future Roadmap
---
- Add user sign-up session
- Product comparison based on prices and product features
- Chat channel

:sparkles: Contributors
---
<center>
  <table>
  <tr>
    <td align="center"><a href="https://github.com/m-payal"><img src="https://avatars.githubusercontent.com/u/51577440?v=4" width="100px;" alt=""/><br /><sub><b>Payal Mehta</b></sub></a></td>
    <td align="center"><a href="https://github.com/Prathmesh2498"><img src="https://avatars.githubusercontent.com/u/46598699?v=4" width="100px;" alt=""/><br /><sub><b>Prathmesh Deshpande</b></sub></a></td>
    <td align="center"><a href="https://github.com/sshrutii"><img src="https://avatars.githubusercontent.com/u/58786334?v=4" width="100px;" alt=""/><br /><sub><b>Shruti Yadav</b></sub></a></td>
    <td align="center"><a href="https://github.com/sumedh-git"><img src="https://avatars.githubusercontent.com/u/58886133?v=4" width="100px;" alt=""/><br /><sub><b>Sumedh Limurkar</b></sub></a></td>
  </tr>
</table>
</center>

## 🙏 Acknowledgements <a name="Acknowledgement"></a>
We would like to thank Professor Dr Timothy Menzies for helping us understand the process of building a good Software Engineering project. We would also like to thank the teaching assistants Xiao Ling, Andre Lustosa, Kewen Peng, Weichen Shi for their support throughout the project.

We would also like to extend our gratitude to previous group : [https://github.com/abhi934/CSC510_Project2_slash-phase3](url)
- [https://streamlit.io/](https://streamlit.io/)
- [https://shields.io/](https://shields.io/)


