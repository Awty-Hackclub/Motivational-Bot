FROM python:3.8

WORKDIR /app

COPY . . 

RUN pip3 install discord pyyaml

CMD python3 main.py 