FROM python:3.9

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin

RUN mkdir -p /usr/src/logs
RUN mkdir -p /usr/src/app/static

EXPOSE 8000

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 settings.wsgi:application

#ENTRYPOINT ["./docker-entrypoint.sh"]
