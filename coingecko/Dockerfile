FROM python:3

RUN apt-get install python-dev


RUN pip install pycoingecko
RUN pip install flask

ADD get.py /usr/local/bin/

CMD ["python", "/usr/local/bin/get.py"]