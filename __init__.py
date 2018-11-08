from .minigun_requests import requests
from .minigun_requests import get_output_from_url
from .minigun_requests import get_output_from_url_iter
from .minigun_requests import get_left_balance
from .example import example as _example


def run_example(email='trial', password='trial'):
    _example(email=email, password=password)
