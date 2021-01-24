FROM python:alpine

RUN apk update && apk add grep

COPY . /app/.

WORKDIR /app

RUN mkdir /opt/rmxgrep && chmod 755 /app ; chmod 755 /opt/rmxgrep

COPY search_corpus.sh /opt/rmxgrep/.

RUN chmod +x /opt/rmxgrep/search_corpus.sh && chmod +x /app/run.sh

ENV SEARCH_CORPUS_SH "/opt/rmxgrep/search_corpus.sh"

# install python dependencies
RUN pip install -U pip && pip install -r requirements.txt

# creating a directory that will contain nltk_data
RUN mkdir /data
VOLUME /data

ENV BROKER_HOST_NAME 'message_broker'

ENV DATA_FOLDER '/data'
