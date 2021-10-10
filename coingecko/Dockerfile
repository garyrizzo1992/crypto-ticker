FROM python:3-buster

RUN pip install pycoingecko
RUN pip install flask

ADD get.py /usr/local/bin/

CMD ["python", "/usr/local/bin/get.py"]