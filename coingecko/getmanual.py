from pycoingecko import CoinGeckoAPI
import flask
import json
from typing import Text

cg = CoinGeckoAPI()

def get_coin_price(coin='bitcoin',vs='usd'):
        return cg.get_price(ids=coin, vs_currencies=vs)

def get_supported_vs_currencies():
        return cg.get_supported_vs_currencies()

def get_coins_list():
        return cg.get_coins_list()


if __name__ == '__main__':
    print(get_supported_vs_currencies())
