FROM python:3.8-alpine

RUN apk update && apk add grep

WORKDIR /app
COPY . /app/.

RUN mkdir /opt/rmxgrep && chmod 755 /app ; chmod 755 /opt/rmxgrep

COPY search_corpus.sh /opt/rmxgrep/.

RUN chmod +x /opt/rmxgrep/search_corpus.sh && chmod +x /app/run.sh

ENV SEARCH_CORPUS_SH '/opt/rmxgrep/search_corpus.sh'

# install python dependencies
RUN pip install -U pip && pip install -r requirements.txt

EXPOSE 8005
