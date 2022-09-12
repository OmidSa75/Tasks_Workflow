from kombu import Queue, Exchange
import celery
import config as cf

# from tasks import *
celery_app = celery.Celery(
    main=cf.CELERY_APP_NAME,
    broker=cf.CELERY_BROKER,
    backend=cf.CELERY_BACKEND,
)
task_routes = {
    'first_app.tasks.*': {
        'queue': 'first_app',
    },
    'second_app': {
        'queue': 'second_app',
    }
}
task_queues = (
    Queue('first_app', routing_key='first_app.tasks.*'),
    Queue('second_app', routing_key='second_app.tasks.*'),
)
celery_app.conf.task_routes = task_routes
celery_app.conf.task_queues = task_queues
celery_app.autodiscover_tasks(['first_app', 'second_app.user'], force=True)
