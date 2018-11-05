# minigun-requests　[![PyPI](https://img.shields.io/pypi/v/minigun.svg)](https://pypi.python.org/pypi/minigun)
Web scraping API to outsource tons of GET & xpath to cloud computing
### Features 
+ Back-end process between 1,000-20,000 requests per minutes like minigun.  
+ Desinged to finish requests within 5 minutes regardless of the amount of requests.  
### Performance Examples
+ 6939 requests to get all stock prices from www.nasdaq.com in 162 seconds  
+ 10000 requests to get new questions from www.stackoverflow.com in 142 seconds  
### Demo
![demo](/images/demo.gif)


## Getting Started
### Installing
```
pip install minigun
```
### Run and make sure your requests works with trial account
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
result=minigun.requests(urls, scraping_xpaths, email='trial', password='trial')
```
* Trial account is up to 1000 requests for one host per day.  
* "trial5" is unlimited trial account but return only 5 results.

## Advanced Usage: What's "validation_xpaths"?
 In tons of requests, responses is not always what you want, such as wrong path, IP blocking, unknown response thru proxy servers. "validation_xpaths" are used to detect unwanted responses and then system can retry with another IP. Default validation_xpaths without specifying are
```
validation_xpaths = [f"boolean({xpath})" for xpath in scraping_xpaths]
# "//div[@id='yyy']" >> "boolean(//div[@id='yyy'])"
```
which means "All specified elements by xpath have to exist in html." So you need to customize and specify validation_xpaths in these cases below:  
```
# Case1: one of scraping_xpaths scrap elements which dosen't exist often
unstable_element_xpath = "//*[@class='sometime_exist']"
validation_xpaths.remove(unstable_element_xpath)

# Case2: scraping_xpaths are weak and high likely to match any response  
scraping_xpaths=['//title',] # most response contain title, not useful to detect unwanted response
validation_xpaths=['boolean(//*[@id='something_unique'])'] # specify something which dose'nt exist in wrong/blocked/unkonwn responses

# Case3: unsure even the url(page) exist or not
validation_xpaths=["boolean(//*[@id='something_when_exist'])"]
```
+  

# 3 dollars & 5 minutes = 10,000 scraping
 (not implemented. don't pay yet)
+ [PayPal page to buy api key](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RBWEMYUS7FCF6)
https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=LLWKDGWZRFQ94 ![Paypal](https://www.paypalobjects.com/webstatic/en_US/i/buttons/PP_logo_h_100x26.png)

[![paypal](https://www.sandbox.paypal.com/en_US/i/btn/btn_cart_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=LLWKDGWZRFQ94)
# System Flowchart
![flowchart](/images/flowchart.png)
