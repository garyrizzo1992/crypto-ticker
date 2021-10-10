FROM python:3.8

##### temp
WORKDIR /tmp/

RUN apt-get install python3-numpy 
RUN git clone https://github.com/ranaroussi/yfinance.git

WORKDIR yfinance

RUN pip install -r requirements.txt -v 
RUN pip install . -v 

##### temp

# RUN pip install yfinance -v

ADD get.py /usr/local/bin/

WORKDIR /home/

ENV COIN=AAVE-USD
ENV PERIOD=1h
ENV INTERVAL=15m

CMD ["python", "/usr/local/bin/get.py"]
