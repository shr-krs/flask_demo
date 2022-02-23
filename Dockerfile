FROM python:3.6

WORKDIR /app

ADD src/requirements.txt /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENTRYPOINT ["flask","run","--host","0.0.0.0","--port","8010","--with-threads"]

# ENTRYPOINT ["yes"]