from cryptocmd import CmcScraper
import os
from datetime import timedelta, date

#Format date
NextDay = date.today() + timedelta(days=1)
PrevDay = date.today() - timedelta(days=1)
print(NextDay,PrevDay)

# initialise scraper with time interval
scraper = CmcScraper(os.environ['COIN'], PrevDay.strftime('%d-%m-%Y'), NextDay.strftime('%d-%m-%Y') )

# get raw data as list of list
headers, data = scraper.get_data()

# get data in a json format
json_data = scraper.get_data("json")

# export the data to csv
scraper.export("csv")

# get dataframe for the data
df = scraper.get_dataframe()