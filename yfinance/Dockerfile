FROM python:3.8

RUN pip install yfinance -v

ADD get.py /usr/local/bin/

WORKDIR /home/

ENV COIN=AAVE-USD
ENV PERIOD=1h
ENV INTERVAL=15m

CMD ["python", "/usr/local/bin/get.py"]
