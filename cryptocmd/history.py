from typing import Text
from cryptocmd import CmcScraper
import flask
import json
from datetime import timedelta, date


def get_todays_data(coin='BTC'):

    NextDay = date.today() + timedelta(days=2)
    PrevDay = date.today() - timedelta(days=2)

    # initialise scraper without time interval
    scraper = CmcScraper(coin.upper(), PrevDay.strftime(
        '%d-%m-%Y'), NextDay.strftime('%d-%m-%Y'))

    # get raw data as list of list
    headers, data = scraper.get_data()

    # get data in a json format
    json_data = scraper.get_data("json")

    # export the data as csv file, you can also pass optional `name` parameter
    # scraper.export("csv", name="aave_all_time")

    # Pandas dataFrame for the same data
    # df = scraper.get_dataframe()

    return json_data


# # flask
# app = flask.Flask(__name__)
# app.config["DEBUG"] = True


# @app.route('/', methods=['GET'])
# def home():
#     coin = flask.request.args.get('coin', default='BTC', type=Text)
#     return get_data(coin)


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=80)
    raw_json = json.loads(get_todays_data())
    print(json.dumps(raw_json, indent=4, sort_keys=True))
