FROM python:3.11

RUN pip install RPi.GPIO

ADD * /app

WORKDIR /app

CMD ["python", "led.py"]