import requests as _requests
import umihico
import time as _time
import random as _random
from lxml.html import fromstring as _fromstring
import base64 as _base64
import ast as _ast
import tqdm as _tqdm
default_header_lang = "ja,en-US;q=0.9,en;q=0.8"


def requests(urls, scraping_xpaths, email='trial', password='trial', validation_xpaths=None,  header_lang=None):
    header_lang = header_lang or default_header_lang
    email = umihico._set_env_value('minigun', email)
    validation_xpaths = validation_xpaths or [
        f"boolean({xpath})" for xpath in scraping_xpaths]
    _raise_if_local_test_fail(urls, scraping_xpaths,
                              validation_xpaths, header_lang)
    request_id = umihico.string.numberize_int(
        umihico.hash_.hash_text(urls[0] + str(_time.time()))[:30])
    url = "http://minigun.umihi.co/" + str(request_id) + '.txt'
    print('If you abort, output will be also generated here.', url)
    args = [email, password, urls, scraping_xpaths,
            validation_xpaths, header_lang, request_id]
    response = _trigger_api('/', *args)
    if response.text != '{"message": "Endpoint request timed out"}' and response.status_code != 200:
        raise Exception(response.text)
    while True:
        output = get_output_from_url(url)
        if output:
            return output
        print("waiting...", url)
        _time.sleep(10)


def get_output_from_url(url='http://minigun.umihi.co/XXXXXXXX'):
    """
    return output thru url when you abort minigun.requests
    outputs will be deleted after a while.
    """
    output_dict = {}
    for chunk_output_dict in get_output_from_url_iter(url):
        output_dict.update(chunk_output_dict)
    return output_dict


def get_output_from_url_iter(url):
    """
    return outputs before they are merged in minigun.requests
    good when outputs are too huge to merge.
    """
    for chunk_index, text in enumerate(_get_output_from_url_chunks_iter(url)):
        header_row, *content_rows = text.split("\n")
        if chunk_index == 0:
            _, *scraping_xpaths = header_row.split(",")
            scraping_xpaths = [x.replace('__(LF)__', '\n').replace(
                '__(CM)__', ',') for x in scraping_xpaths]
        output_dict = {}
        for row_text in content_rows:
            row_text = row_text.replace('__(LF)__', '\n')
            url, *xpath_results = row_text.split(',')
            output_dict[url] = {xpath: _ast.literal_eval(
                result.replace('__(CM)__', ',')) for xpath, result in zip(scraping_xpaths, xpath_results)}
        yield output_dict


def _get_output_from_url_chunks_iter(url):
    """
    original ',' are replaced as '__(CM)__' and new lines are as '__(LF)__'
    """
    response = _requests.get(url)
    if response.status_code != 200:
        return None
    chunk_urls = _ast.literal_eval(
        _base64.b64decode(response.text).decode())
    for chunk_url in _tqdm.tqdm(iterable=chunk_urls, desc='downloading and parsing outputs'):
        chunk_response = _requests.get(chunk_url)
        # print(chunk_response.text)
        text = _base64.b64decode(chunk_response.text).decode()
        yield text


def get_left_balance(email="YOUR PAYPAL EMAIL", password="YOUR PASSWORD"):
    print(_trigger_api("/get-apikey-balance", email, password).text)


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
