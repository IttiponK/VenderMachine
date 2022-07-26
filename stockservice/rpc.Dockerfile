FROM python:3.7.3-alpine3.8
RUN apk add --no-cache mariadb-dev build-base
WORKDIR /code 
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./infrastructure/mysql/connect.py /code/app/infrastructure/mysql/connect.py 
COPY ./hexagonalmodel /code/app/hexagonalmodel
COPY ./mqbroker /code/app/mqbroker
CMD nameko run app.mqbroker.rpc --broker amqp://guest:guest@rabbitmq:5672