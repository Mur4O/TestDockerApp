FROM python:3.12-alpine

RUN mkdir /apps
RUN mkdir /data

COPY main.py main.py
COPY /apps/Regard.py /apps/Regard.py

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "main.py"]