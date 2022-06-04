from requests import get
from conf import *


class Converter:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_currencies(self):
        currency_url = f"/api/v7/currencies?apiKey={API_KEY}"
        currency_data = get(self.base_url + currency_url).json()['results']
        currency_list = list(currency_data.values())

        return currency_list

    def convert_currency(self, currency_1, currency_2, amount):
        convert_url = f"/api/v7/convert?q={currency_1}_{currency_2}&compact=ultra&apiKey={API_KEY}"
        convert_data = get(self.base_url + convert_url).json()

        converted_list = list(convert_data.values())

        if len(converted_list) == 0:
            print("Currency not found")
            return -1

        return format(converted_list[0] * amount, '.2f')
