
# from .conf import BROKER_HOST_NAME, REDIS_PASS

from .conf import RPC_HOST, RPC_PASS, RPC_PORT, RPC_USER, RPC_VHOST
# celery backend related imports
from .conf import (DATABASE_USERNAME, DATABASE_PASSWORD, MONGODB_LOCATION,
                   RPC_DATABASE)


# broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'
_url = f'amqp://{RPC_USER}:{RPC_PASS}@{RPC_HOST}:{RPC_PORT}/{RPC_VHOST}'

# _url = f'redis://:{REDIS_PASS}@{BROKER_HOST_NAME}:6379/0'

BROKER_URL = _url
# CELERY_RESULT_BACKEND = _url

CELERY_RESULT_BACKEND = 'mongodb://'
CELERY_MONGODB_BACKEND_SETTINGS = {
    'host': MONGODB_LOCATION,
    'user': DATABASE_USERNAME,
    'password': DATABASE_PASSWORD,
    'database_name': RPC_DATABASE
}

CELERY_RESULT_PERSISTENT = True

CELERY_IMPORTS = ('rmxgrep.task', )

CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_ROUTES = {

    'rmxgrep.task.*': {'queue': 'rmxgrep'}
}
