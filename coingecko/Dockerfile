FROM python:3

USER root 

RUN pip install pycoingecko
RUN pip install pip install flask

ADD get.py /usr/local/bin/

CMD ["python", "/usr/local/bin/get.py"]