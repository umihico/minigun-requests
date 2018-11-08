 # minigun-requests
> Web scraping API to outsource tons of GET & xpath to cloud computing  

[![PyPI](https://img.shields.io/pypi/v/minigun.svg)](https://pypi.python.org/pypi/minigun)　[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
### Features
+ Back-end process your requests between 1,000-20,000 rounds per minute like minigun's rate of fire.  
+ Automatic concurrency scaling design to finish requests within 10 minutes regardless of the amount.  

![demo](/images/demo.gif)![flowchart](/images/flowchart.png)
### Performance Examples
+ 6911 requests to get all stock prices from www.nasdaq.com in 72 seconds  
+ 34453 requests to get all available rental names in tokyo from www.suumo.jp in 201 seconds  
+ 100000 requests to get new question titles from www.stackoverflow.com in 81 seconds  
## Getting Started
### Installing
```python
pip install minigun
```
### Running the tests enough with trial account
```python
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

# if you abort while waiting, use get_output_from_url function to get result
result=minigun.get_output_from_url("http://minigun.umihi.co/DISTPLAYED_NUMBERS.txt")
```
+ I personally recommend [Xpath Helper](https://chrome.google.com/webstore/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl) to find xpath, and this article [Tips for strong XPath](https://developers.perfectomobile.com/pages/viewpage.action?pageId=13893679)
+ If you get 'error' in result, please read [When you get error from result](#when-you-get-error-from-result)  
+ Trial account is up to 1000 requests per each host per 24 hours.  
+ "trial5" is unlimited trial account but return only 5 results.  

### 1 cent = 100 requests! from $3
　If you are sure your arguments works well and willing to do more requests, please go to [PayPal page](https://ic8ntngzk4.execute-api.us-west-2.amazonaws.com/stage/paypal-topup-page) and top-up.
After payment, PayPal's instant payment notification triggers immediately registering and top-up function.
Then you can replace arguments to your PayPal email address and password you set.
```python
import minigun
minigun.requests(urls, scraping_xpaths, email='YOUR PAYPAL EMAIL', password='YOUR PASSWORD')
```

## Advanced Usage
### Can I know how much my balance left?
This command will print your balance.
```python
import minigun
minigun.get_left_balance(email="YOUR PAYPAL EMAIL", password="YOUR PASSWORD")
```
### Can I change my password?
You can set and change only when you top-up. Only the newest password works.
### When you get error from result
　If you get nested dictionary as output correctly but some values are "error", they happen when one of "validation_xpaths" always return False from the parsed html regardless of retrying many times with IP rotation. "validation_xpaths" are optional argument which is generated according to "scraping_xpaths" by default like this.
```python
validation_xpath = "boolean(" + scraping_xpath + ")"
```
This default validation_xpaths with 'Error' means "one of scraping_xpaths couldn't find any elements." This is what's happening in back-end. Please check the url and make sure the all scraping_xpaths pick at least one elements from the page. If you notice the element you want is not always there, you need to customize validation_xpaths.  

　Why are validation_xpaths neccesary? It's because in tons of requests, responses is not always what you want. They are busy one, IP blocking, and non-related responses from proxy servers. "validation_xpaths" are used to detect such unwanted responses and then process can retry with another IP. This is common problem of web scraping (some websites block you even if your rate of access is slow)
### Examples of "validation_xpaths"
　Best practice is simplifying validation_xpaths, like specifying only elements which exist definitely and unique, not in busy/blocked/non-related response. For example if you are scarping personal profile webpage, "Name" sounds definite, but "email" and "LinkedIn" sounds optional. More special case examples are blow:
```python
# Case1: scraping_xpaths are weak and high likely to match any responses
scraping_xpaths=['//title', ] 
# it's fine if you want only titles, but not useful to kick unwanted responses out.
validation_xpaths = ['boolean(//*[@id='something_unique'])', ] 
# specify something which doesn't exist in busy/wrong/blocked/unkonwn responses

# Case2: unsure the url(page) exist or not
# you can still scrap when 404 error if the content is html. telling that 404 is expected response stop retrying
validation_xpaths = ["boolean(//*[@id='something_unique_when_200']|//*[@id='something_unique_when_404'])", ] 
# use "|" as "or"

# Case3: error page is quite similar with normal response
validation_xpaths = ["not(//*[@id='busy_page_unique_element']", ] 
# detect element which appear when error response with "not" function
```
## Contributing
+ Any language matter advise would be greatly appreciated
+ Feel free to tell me features you want and errors you are facing
