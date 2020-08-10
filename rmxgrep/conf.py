
import os


BROKER_HOST_NAME = os.environ.get('BROKER_HOST_NAME')

SEARCH_TEXT_SH = os.environ.get('SEARCH_CORPUS_SH')

# celery, redis (auth access) configuration
REDIS_PASS = os.environ.get('REDIS_PASS')
