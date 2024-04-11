FROM python:3.11-slim

USER root

WORKDIR /home/project
RUN apt-get update && apt-get -y install make

COPY abas abas
COPY auth auth
COPY scrapping scrapping
COPY Makefile  Makefile
COPY requirements.txt requirements.txt 
COPY run.py run.py 
COPY database.py database.py 
COPY boot.sh boot.sh

RUN make install
RUN chmod +x boot.sh

EXPOSE 5000

ENTRYPOINT ["/home/project/boot.sh"]