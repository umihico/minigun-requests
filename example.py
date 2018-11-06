"""pip install minigun"""
import minigun
import pprint


def example():

    # pip install minigun
import minigun
import pprint
urls = [
    "https://www.nasdaq.com/symbol/amzn",
    "https://www.nasdaq.com/symbol/googl",
    "https://www.nasdaq.com/symbol/aapl",
    "https://www.nasdaq.com/symbol/fb",
    "https://www.nasdaq.com/symbol/nflx",
    "https://www.nasdaq.com/symbol/msft",
    "https://www.nasdaq.com/symbol/nvda",
]
scraping_xpaths = [
    "//div[@id='qwidget_lastsale']",
    "//div[@id='qwidget_percent']",
]
pprint.pprint(minigun.requests(urls, scraping_xpaths,
                               email='trial', password='trial'))

    result = minigun.requests(urls, scraping_xpaths,
                              email='trial', password='trial')
    pprint.pprint(result)
    pprint.pprint(type(result))


if __name__ == '__main__':
    example()
    """ ***output will be like this***
    If you abort, output will be also generated here. http://minigun.umihi.co/XXXXXXXXXXXXX.txt
    waiting... http://minigun.umihi.co/XXXXXXXXXXXXX.txt
    {'https://www.nasdaq.com/symbol/aapl': {"//div[@id='qwidget_lastsale']": ['$207.48'],
                                            "//div[@id='qwidget_percent']": ['6.63%']},
     'https://www.nasdaq.com/symbol/amzn': {"//div[@id='qwidget_lastsale']": ['$1665.53'],
                                            "//div[@id='qwidget_percent']": ['unch']},
     'https://www.nasdaq.com/symbol/fb': {"//div[@id='qwidget_lastsale']": ['$150.35'],
                                          "//div[@id='qwidget_percent']": ['0.92%']},
     'https://www.nasdaq.com/symbol/googl': {"//div[@id='qwidget_lastsale']": ['$1071.49'],
                                             "//div[@id='qwidget_percent']": ['1.33%']}}
    <class 'dict'>
    """
