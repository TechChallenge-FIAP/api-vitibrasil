FROM python:3.11-slim

USER root

WORKDIR /home/project
RUN apt-get update && apt-get -y install make

COPY crud crud
COPY rest_api rest_api
COPY scrapping scrapping
COPY services services
COPY Makefile requirements.txt boot.sh ./

RUN mkdir tmp
RUN make install
RUN chmod +x boot.sh

EXPOSE 5000

ENTRYPOINT ["/home/project/boot.sh"]