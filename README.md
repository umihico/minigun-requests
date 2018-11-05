 # minigun-requests
> Web scraping API to outsource tons of GET & xpath to cloud computing  

[![PyPI](https://img.shields.io/pypi/v/minigun.svg)](https://pypi.python.org/pypi/minigun)　[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
### Features
+ API fire your requests by back-end between 1,000-20,000 rounds per minute like minigun.  
+ Desinged to finish requests within 5 minutes regardless of the amount.  

![flowchart](/images/flowchart.png)
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
### Running the tests enough with trial account
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

+ If you get 'error' in result, look at [Advanced Usage](#advanced-usage)  
+ Trial account is up to 1000 requests for one host per day.  
+ "trial5" is unlimited trial account but return only 5 results.  

### 1 cent = 100 requests! from $3
　If you are sure your arguments works well and willing to do more requests, please go to [PayPal page](#https://ic8ntngzk4.execute-api.us-west-2.amazonaws.com/stage/paypal-topup-page) and top-up.
After payment, PayPal's instant payment notification triggers immediately registering and top-up function.
Then you can replace arguments to your PayPal email address and password you set.
```
import minigun
minigun.requests(urls, scraping_xpaths, email='YOUR PAYPAL EMAIL', password='YOUR PASSWORD')
```

## Advanced Usage
### What's "validation_xpaths"?
　In tons of requests, responses is not always what you want, such as incorrect path, IP blocking, non-related response from proxy servers. "validation_xpaths" are used to detect unwanted responses and then process can retry with another IP. Default validation_xpaths by default are
```
validation_xpaths = [f"boolean({xpath})" for xpath in scraping_xpaths]
# "//div[@id='yyy']" >> "boolean(//div[@id='yyy'])"
```
which means "All scraping_xpaths have to find at least one element, otherwise retry." If you don't like this behavior, you need to customize validation_xpaths. Typical cases are below:  
```
# Case1: one of scraping_xpaths scrap elements which dosen't exist often
unstable_element_xpath = "//*[@class='sometime_exist']"
validation_xpaths = validation_xpaths or [f"boolean({xpath})" for xpath in scraping_xpaths if xpath != unstable_element_xpath]

# Case2: scraping_xpaths are weak and high likely to match any response  
scraping_xpaths=['//title',] # most response contain title, not useful to detect unwanted response
validation_xpaths=['boolean(//*[@id='something_unique'])',] # specify something which dose'nt exist in wrong/blocked/unkonwn responses

# Case3: unsure even the url(page) exist or not
validation_xpaths=["boolean(//*[@id='something_when_exist']|//*[@id='something_when_not_exist'])",] # use "|" as "or"

# Case4: servers spit out busy response depends on IP and similar with normal response
validation_xpaths=["not(//*[@id='busy_page_unique_element']"] # use "not" to detect busy response's element
```
## Contributing
+ I appreciate any language matter advice in this README
+ tell me your features requests you want
