FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install -r requirements.txt

COPY ./ /usr/src/app

CMD ["python", "/usr/src/app/http/app.py"]