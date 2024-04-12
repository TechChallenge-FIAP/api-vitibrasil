FROM python:3.11-slim

USER root

WORKDIR /home/project
RUN apt-get update && apt-get -y install make

COPY abas abas
COPY auth auth
COPY scrapping scrapping
COPY crud crud
COPY Makefile requirements.txt run.py database.py boot.sh swagger.py ./

RUN mkdir tmp
RUN make install
RUN chmod +x boot.sh

EXPOSE 5000

ENTRYPOINT ["/home/project/boot.sh"]