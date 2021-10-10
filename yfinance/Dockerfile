FROM python:buster

RUN pip install yfinance
RUN pip install plotly

ADD get.py /usr/local/bin/

WORKDIR /home/

ENV COIN=AAVE-USD
ENV PERIOD=1h
ENV INTERVAL=15m

CMD ["python", "/usr/local/bin/get.py"]
