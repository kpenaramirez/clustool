FROM python:3.10.6

WORKDIR /app
COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD ["gunicorn", "main:server", "--bind", "0.0.0.0:8000"]