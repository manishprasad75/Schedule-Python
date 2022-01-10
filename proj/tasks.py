from __future__ import absolute_import

from celery import Celery
from celery.schedules import crontab

from datetime import timedelta

"""
NOTE: To register task with celery work, pass tasks modules - full path to with Celery -> include param
or Assign with CELERY_IMPORTS 
https://docs.celeryproject.org/en/3.1/configuration.html#celery-imports
"""
celery = Celery('proj', include=["proj.bg_task"])

celery.conf.CELERY_ENABLE_UTC = True


celery.conf.CELERY_ANNOTATIONS = {}

celery.conf.CELERYD_PREFETCH_MULTIPLIER = 1


# mongodb config
# celery.conf.CELERY_RESULT_BACKEND = "mongodb://localhost:27017"
# celery.conf.CELERY_MONGODB_BACKEND_SETTINGS = {
#     "database": "celery_result",
#     "taskmeta_collection": "taskmeta_collection"
# }

# celery.conf.CELERY_RESULT_BACKEND = "db+postgresql://chandanprasad:password@localhost:5432/celery_db"

celery.conf.CELERY_ROUTES = {
    "bg_task.show_current_time": {"queue": "TASKQ"},
}

celery.conf.BROKER_URL = "redis://localhost:6379/1"
celery.conf.BROKER_CONNECTION_MAX_RETRIES = 0
celery.conf.BROKER_FAILOVER_STRATEGY = "round-robin"
celery.conf.BROKER_HEARTBEAT = 10
celery.conf.BROKER_CONNECTION_MAX_RETRIES = 0

celery.conf.CELERY_ALWAYS_EAGER = False
celery.conf.CELERY_IGNORE_RESULT = False
celery.conf.CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
celery.conf.CELERY_MESSAGE_COMPRESSION = "gzip"
celery.conf.CELERY_RESULT_SERIALIZER = 'json'
celery.conf.CELERY_TASK_SERIALIZER = 'json'
celery.conf.CELERY_EVENT_SERIALIZER = 'json'
celery.conf.CELERY_ENABLE_REMOTE_CONTROL = False
celery.conf.CELERYD_POOL_RESTART = False
celery.conf.CELERYD_TASK_SOFT_TIME_LIMIT = 300




celery.conf.CELERYBEAT_LOG_LEVEL = 'DEBUG'
celery.conf.CELERYBEAT_LOG_FILE = '/tmp/rounds_celerybeat.log'
celery.conf.LOG_LEVELS = "DEBUG"
celery.conf.CELERYD_LOG_LEVEL = "DEBUG"
celery.conf.CELERYD_LOG_FILE = "/tmp/rounds_celery_d.log"


celery.conf.CELERYBEAT_SCHEDULE = {
    'ShowCurrentTime': {
        'task': 'proj.bg_task.sendEmail',
        'schedule': timedelta(minutes=1),
        'args': (),
    },
}

celery.conf.CELERY_TIMEZONE = 'UTC'
if __name__ == '__main__':
    celery.start()

# way to start Celery
# cd rounds_api/kernel
# celery worker --app=kernel.task --loglevel=debug --logfile=/tmp/spiff_workers.log --autoscale=10,3 &


# way to kill Celery
# ps auxww | grep 'celery worker' | awk '{print $2}' | xargs kill -9
# celery doc reference 3.1.x
