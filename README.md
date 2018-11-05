# minigun-requests　[![PyPI](https://img.shields.io/pypi/v/minigun.svg)](https://pypi.python.org/pypi/minigun)
Web scraping API to outsource tons of GET & xpath to cloud computing
### Features 
+ Back-end process between 1,000-20,000 requests per minutes like minigun.  
+ Desinged to finish requests within 5 minutes regardless of the amount of requests.  
### Performance Examples
+ 6939 requests to get all stock prices from www.nasdaq.com in 162 seconds  
+ 10000 requests to get new questions from www.stackoverflow.com in 142 seconds  

![demo](/images/demo.gif)


## Getting Started
### Installing
```
pip install minigun
```
### test with trial account for free
```
import minigun
urls = [
    "https://www.xxx.com/pages/1",
    "https://www.xxx.com/pages/2",
    "https://www.xxx.com/pages/3",
]
scraping_xpaths = [
    "//div[@id='xxx']",
    "//div[@id='yyy']",
]
minigun.requests(urls, scraping_xpaths, email='trial', password='trial')
```
*Trial account is up to 1000 requests for one host per day.
*email='trial5' is unlimited trial but return only 5 results.
# 3 dollars & 5 minutes = 10,000 scraping
 (not implemented. don't pay yet)
+ [PayPal page to buy api key](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RBWEMYUS7FCF6)
https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=LLWKDGWZRFQ94 ![Paypal](https://www.paypalobjects.com/webstatic/en_US/i/buttons/PP_logo_h_100x26.png)

[![paypal](https://www.sandbox.paypal.com/en_US/i/btn/btn_cart_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=LLWKDGWZRFQ94)
# System Flowchart
![flowchart](/images/flowchart.png)
