FROM python:3

ADD client.py /

RUN pip install pystrich

CMD [ "python", "./client.py" ]