FROM python:3.8
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# COPY ./infrastructure/rabbitmq /code/app/infrastructure/rabbitmq
COPY ./infrastructure/mysql/connect.py /code/app/infrastructure/mysql/connect.py 
COPY ./rest /code/app/rest
COPY ./hexagonalmodel /code/app/hexagonalmodel
CMD ["uvicorn", "app.rest.main:app", "--host", "0.0.0.0", "--port", "8001"]