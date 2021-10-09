import os

# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
# import plotly.graph_objs as go


data = yf.download(tickers=os.environ['COIN'], period = os.environ['PERIOD'], interval = os.environ['INTERVAL'])

print(data)