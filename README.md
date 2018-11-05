 # minigun-requests
> Web scraping API to outsource tons of GET & xpath to cloud computing  

[![PyPI](https://img.shields.io/pypi/v/minigun.svg)](https://pypi.python.org/pypi/minigun)
### Features
+ fire your requests between 1,000-20,000 rounds per minutes like minigun.  
+ Desinged to finish requests within 5 minutes regardless of the amount of requests.  

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
### Running the tests with trial account
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
If you get 'error' in result, look at [Advanced Usage](#advanced-usage-whats-validation_xpaths)

### 3 dollars & 5 minutes = 30,000 times requests!
If you are sure your arguments works well and willing to do more requests, please go to [PayPal page](#https://ic8ntngzk4.execute-api.us-west-2.amazonaws.com/stage/paypal-topup-page) and top-up.
After payment, PayPal's instant payment notification triggers immediately registering and top-up function.
Then you can replace arguments to your PayPal email address and password you set.
```
import minigun
minigun.requests(urls, scraping_xpaths, email='YOUR PAYPAL EMAIL', password='YOUR PASSWORD')
```


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
validation_xpaths = validation_xpaths or [f"boolean({xpath})" for xpath in scraping_xpaths if xpath != unstable_element_xpath]

# Case2: scraping_xpaths are weak and high likely to match any response  
scraping_xpaths=['//title',] # most response contain title, not useful to detect unwanted response
validation_xpaths=['boolean(//*[@id='something_unique'])',] # specify something which dose'nt exist in wrong/blocked/unkonwn responses

# Case3: unsure even the url(page) exist or not
validation_xpaths=["boolean(//*[@id='something_when_exist']|//*[@id='something_when_not_exist'])",] # use "|" as "or"

# Case4: servers spit out busy response depends on IP and similar with normal response
validation_xpaths=["not(//*[@id='busy_page_unique_element']"] # use "not" to detect busy response's element
```
