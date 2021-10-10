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

# flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/get_coin_price', methods=['GET'])
def coinprice():
    coin = flask.request.args.get('coin', default='bitcoin', type=Text)
    vs = flask.request.args.get('vs', default='usd', type=Text)
    print(get_coin_price(coin,vs))

@app.route('/get_supported_vs_currencies', methods=['GET'])
def getvscurrencies():
    print(get_supported_vs_currencies())

@app.route('/get_coins_list', methods=['GET'])
def coinlist():
    print(get_coins_list())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
    # raw_json = json.loads(get_todays_data())
    # print(json.dumps(raw_json, indent=4, sort_keys=True))
