
from celery import Celery

from . import celeryconf

celery = Celery('rmxgrep')

celery.config_from_object(celeryconf)

