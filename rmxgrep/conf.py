
import os


BROKER_HOST_NAME = os.environ.get('BROKER_HOST_NAME')

SEARCH_TEXT_SH = os.environ.get('SEARCH_CORPUS_SH')

# celery, redis (auth access) configuration
REDIS_PASS = os.environ.get('REDIS_PASS')


# RabbitMQ configuration
# RabbitMQ rpc queue name
# These values are defined on the level of docker-compose.
RPC_QUEUE_NAME = os.environ.get('RPC_QUEUE_NAME', 'rmxgrep')

# login credentials for RabbitMQ.
RPC_PASS = os.environ.get('RABBITMQ_DEFAULT_PASS')
RPC_USER = os.environ.get('RABBITMQ_DEFAULT_USER')
RPC_VHOST = os.environ.get('RABBITMQ_DEFAULT_VHOST')

# the host to which the rpc broker (rabbitmq) is deployed
RPC_HOST = os.environ.get('RABBITMQ_HOST')
RPC_PORT = os.environ.get('RABBITMQ_PORT', 5672)

# mongodb celery backend
DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
MONGO_PORT = os.environ.get('MONGO_PORT')
MONGODB_LOCATION = os.environ.get('MONGODB_LOCATION')
RPC_DATABASE = os.environ.get('RPC_DATABASE')
RPC_COLLECTION = os.environ.get('RPC_COLLECTION')
