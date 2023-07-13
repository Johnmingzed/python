FROM python:3.11

WORKDIR /usr/src/app/jeu

RUN pip install pygame

ADD . ..

CMD ["python", "jeu.py"]