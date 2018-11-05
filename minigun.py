import requests as _requests
import umihico
import time as _time
import random as _random
from lxml.html import fromstring as _fromstring
import base64 as _base64
import ast as _ast
default_header_lang = "ja,en-US;q=0.9,en;q=0.8"


def requests(urls, scraping_xpaths, email='trial', password='trial', validation_xpaths=None,  header_lang=None):
    header_lang = header_lang or default_header_lang
    email = umihico._set_env_value('minigun', email)
    validation_xpaths = validation_xpaths or [
        f"boolean({xpath})" for xpath in scraping_xpaths]
    # _raise_if_local_test_fail(urls, scraping_xpaths,
    #                           validation_xpaths, header_lang)
    request_id = umihico.string.numberize_int(
        umihico.hash_.hash_text(urls[0] + str(_time.time()))[:30])
    url = "http://minigun.umihi.co/" + str(request_id) + '.txt'
    print('If you abort, output will be also generated here.', url)
    args = [email, password, urls, scraping_xpaths,
            validation_xpaths, header_lang, request_id]
    response = _trigger_api('/', *args)
    if response.text != '{"message": "Endpoint request timed out"}':
        response.raise_for_status()
    while True:
        output = get_output_from_url(url)
        if output:
            return output
        print("waiting...", url)
        _time.sleep(10)


def get_output_from_url(url='http://minigun.umihi.co/XXXXXXXX'):
    response = _requests.get(url)
    if response.status_code == 200:
        text = _base64.b64decode(response.text).decode()
        return _ast.literal_eval(text)
    else:
        False


def create_apikey():
    return _trigger_api("/create-apikey", payload)


def get_apikey_balance():
    return _trigger_api("/get-apikey-balance", payload)


def _raise_if_local_test_fail(urls, scraping_xpaths, validation_xpaths, header_lang):
    print("local sample scraping test start")
    testing_urls = _random.sample(urls, 3)
    xpaths_bools = [
        *[(x, True) for x in validation_xpaths],
        *[(x, False) for x in scraping_xpaths]
    ]
    # print(len(xpaths_bools), len(testing_urls))
    for url in testing_urls:
        # print(url)
        lxml = _fromstring(umihico.scraping.requests_.get(
            url, header_lang=header_lang, timeout=30).text,)
        for xpath, is_validation_xpath in xpaths_bools:
            try:
                lxml_result = lxml.xpath(xpath)
            except Exception as e:
                raise Exception(
                    f"xpath:'{xpath}' is invalid xpath")
            if is_validation_xpath and not isinstance(lxml_result, bool):
                raise Exception(
                    f"xpath:'{xpath}' returns '{lxml_result}', not boolean (True or False) output.")
            if is_validation_xpath and isinstance(lxml_result, bool) and not lxml_result:
                raise Exception(
                    f"url:'{url}' and xpath:'{xpath}' returns False without using proxy server.")
            # print(xpath, umihico.scraping.lxml_.elements_to_strings_list(lxml_result))
    print("local sample scraping test end")


def _trigger_api(path, *args):
    payload = umihico.aws.lambda_.args2payload(*args)
    api_endpoint = "https://ic8ntngzk4.execute-api.us-west-2.amazonaws.com/stage"
    return umihico.aws.lambda_.trigger_via_apigateway(
        api_endpoint + path, payload=payload)


if __name__ == '__main__':
    urls = [
        "https://www.nasdaq.com/symbol/amzn",
        "https://www.nasdaq.com/symbol/googl",
        "https://www.nasdaq.com/symbol/aapl",
        "https://www.nasdaq.com/symbol/fb",
    ]
    scraping_xpaths = [
        "//div[@id='qwidget_lastsale']",
        "//div[@id='qwidget_percent']",
    ]
    print(requests(urls, scraping_xpaths, email='trial', password='trial'))
