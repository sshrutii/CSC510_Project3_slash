"""
Copyright (c) 2021 Rohan Shah
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Slash
"""

# package imports
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from threading import Thread

# local imports
import src.formattr as form
from src.configs_mt import AMAZON, WALMART, COSTCO, BESTBUY, scrape_ebay, scrape_target

class search(Thread):
    def __init__(self, query, config):
        self.result = {}
        self.query = query
        self.config = config
        super(search,self).__init__()
        
    def run(self):
        """Scrape the given config for a specific item

        Parameters
        ----------
        query: str
            Query of item we are looking for
        config: dict
            Configuration for site we are scraping

        Returns
        ----------
        products: list
            List of items returned from website
        """
        if self.config['site'] == 'costco':
            self.query = form.formatSearchQueryForCostco(self.query)
        else:
            self.query = form.formatSearchQuery(self.query)
        URL = self.config['url'] + self.query

        # fetch url
        page = self.httpsGet(URL)
        if not page:
            self.result = []

        # begin parsing page content
        results = page.find_all(self.config['item_component'], self.config['item_indicator'])
        products = []
        for res in results:
            title = res.select(self.config['title_indicator'])
            price = res.select(self.config['price_indicator'])
            link = res.select(self.config['link_indicator'])
            product = form.formatResult(self.config['site'], title, price, link)
            if product['title'] != '' and product['price'] != '' and product['link'] != '':
                products.append(product)
        self.result = products

    def httpsGet(self, URL):
        """makes HTTP called to the requested URL with custom headers

        Parameters
        ----------
        URL: str
            URL we are sending request to

        Returns
        ----------
        soup: str
            HTML of page we requested
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',  # noqa: E501
            'Accept-Encoding': 'gzip, deflate',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '0',
            'Cache-Control': 'no-cache'
        }
        s = requests.Session()
        page = s.get(URL, headers=headers)
        if page.status_code == 200:
            soup1 = BeautifulSoup(page.content, 'html.parser')
            return BeautifulSoup(soup1.prettify(), 'html.parser')
        else:
            # TODO add logger
            return None


def scrape(args, scrapers):
    """Conduct scraping of sites based on scrapers

    Parameters
    ----------
    args: dict
        Dictionary of arguments used for scraping

        search : str [query to search on]
        sort : str [sort by column name ; pr - price]
        des : boolean [True for reverse, False for asc]
        num : number of rows in the output
    scrapers: list
        List of scrapers to use

    Returns
    ----------
    overall: list
        List of items returned from scrapers
    """
    print('Start Time: ', datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    query = args['search']

    overall = []
    scrapers = sorted(scrapers)

    i = 0
    while i < len(scrapers):
        if scrapers[i] == 'amazon':
            t_az = search(query, AMAZON)
            t_az.start()
            i += 1
            if i == len(scrapers):
                break
        if scrapers[i] == 'bestbuy':
            print("Bestbuy")
            t_bb = search(query, BESTBUY)
            t_bb.start()
            i += 1
            if i == len(scrapers):
                break
        if scrapers[i] == 'costco':
            t_cc = search(query, COSTCO)
            t_cc.start()
            i += 1
            if i == len(scrapers):
                break
        if scrapers[i] == 'ebay':
            t_eb = scrape_ebay(query)    
            t_eb.start()
            i += 1
            if i == len(scrapers):
                break
        if scrapers[i] == 'target':
            t_tg = scrape_target(query)
            t_tg.start()
            i += 1
            if i == len(scrapers):
                break
        if scrapers[i] == 'walmart':
            t_wm = search(query, WALMART)
            t_wm.start()
            i += 1
            if i == len(scrapers):
                break
        else:
            i += 1
            if i == len(scrapers):
                break

    i = 0
    while i < len(scrapers) :
        if scrapers[i] == 'amazon':
            t_az.join()
            i += 1
            for sort_by in args['sort']:
                local = form.sortList(t_az.result, sort_by, args['des'])
            overall.extend(local)
            if i == len(scrapers):
                break
        if scrapers[i] == 'bestbuy':
            t_bb.join()
            i += 1
            for sort_by in args['sort']:
                local = form.sortList(t_bb.result, sort_by, args['des'])
            overall.extend(local)
            if i == len(scrapers):
                break
        if scrapers[i] == 'costco':
            t_cc.join()
            i += 1
            for sort_by in args['sort']:
                local = form.sortList(t_cc.result, sort_by, args['des'])
            overall.extend(local)
            if i == len(scrapers):
                break
        if scrapers[i] == 'ebay':
            t_eb.join()
            i += 1
            for sort_by in args['sort']:
                local = form.sortList(t_eb.result, sort_by, args['des'])
            overall.extend(local)
            if i == len(scrapers):
                break
        if scrapers[i] == 'target':
            t_tg.join()
            i += 1
            for sort_by in args['sort']:
                local = form.sortList(t_tg.result, sort_by, args['des'])
            overall.extend(local)
            if i == len(scrapers):
                break
        if scrapers[i] == 'walmart':
            t_wm.join()
            i += 1
            for sort_by in args['sort']:
                local = form.sortList(t_wm.result, sort_by, args['des'])
            overall.extend(local)
            if i == len(scrapers):
                break
        else:
            i += 1
            if i == len(scrapers):
                break


    for sort_by in args['sort']:
        overall = form.sortList(overall, sort_by, args['des'])

    print('Before return time: ', datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    
    return overall
