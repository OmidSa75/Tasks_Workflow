from kombu import Queue, Exchange
import celery
import config as cf

# from tasks import *
celery_app = celery.Celery(
    main=cf.CELERY_APP_NAME,
    broker=cf.CELERY_BROKER,
    backend=cf.CELERY_BACKEND,
    include=['tasks']
)
celery_app.conf.task_queues = (
    Queue('default', routing_key='tasks'),
    Queue('custom', routing_key='custom')
)
celery_app.conf.task_routes = {'tasks.*': {'queue': 'custom'}}
celery_app.autodiscover_tasks()