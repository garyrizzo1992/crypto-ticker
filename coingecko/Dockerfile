FROM python:3.6

USER root 
RUN rm -rf /usr/bin/lsb_release

RUN pip install pycoingecko -v

ADD get.py /usr/local/bin/

CMD ["python", "/usr/local/bin/get.py"]