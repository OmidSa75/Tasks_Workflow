import celery
from celery.result import allow_join_result

CELERY_APP_NAME = 'test_app'
CELERY_BROKER = 'redis://192.168.1.114:6379/0'
CELERY_BACKEND = 'redis://192.168.1.114:6379/1'
celery_app_test = celery.Celery(
    CELERY_APP_NAME,
    backend=CELERY_BACKEND,
    broker=CELERY_BROKER,
)


def test_shared_task():
    task = celery_app_test.send_task('simple_task', args=('hello world',),
                                     queue='first_app')
    with allow_join_result():
        simple_task_result = task.get(timeout=1)
    assert simple_task_result == 'simple_task'

    task = celery_app_test.send_task('register_user', args=('omid',), queue='second_app')
    with allow_join_result():
        simple_task_result = task.get(timeout=1)
    assert simple_task_result == 'register_user'
