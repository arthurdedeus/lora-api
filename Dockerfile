FROM python:3.6-onbuild

RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin

RUN mkdir -p /usr/src/logs
RUN mkdir -p /usr/src/app/static

EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]