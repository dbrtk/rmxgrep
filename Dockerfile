FROM python:3.7-alpine

RUN apk update && apk add grep

# Creating a user tu run the process
RUN addgroup -S rmxuser && adduser -S rmxuser -G rmxuser

# creating a directory that will hold data
# RUN mkdir -p /data/corpus
#	&& chown -R rmxuser:rmxuser /data

# VOLUME /data

WORKDIR /app
COPY . /app/.

RUN mkdir /opt/rmxgrep && chmod 755 /app


COPY search_corpus.sh /opt/rmxgrep/.

RUN chmod +x /opt/rmxgrep/search_corpus.sh \
    && chown -R rmxuser:rmxuser /app \
    && chown -R rmxuser:rmxuser /opt/rmxgrep

# the code below is python related.
RUN pip install -U pip && pip install -r requirements.txt

USER rmxuser

EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "/app/app.py"]
