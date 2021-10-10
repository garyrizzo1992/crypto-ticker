FROM python

RUN pip install pycoingecko -v

ADD get.py /usr/local/bin/

CMD ["python", "/usr/local/bin/get.py"]