FROM python:3.9
ENV PYTHONUNBUFFERED=1
ENV TZ Europe/Moscow
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/