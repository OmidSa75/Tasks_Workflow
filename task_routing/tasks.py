from celery import shared_task


@shared_task(name='simple_task')
def simple_task(message: str) -> str:
    print(message)
    return "OK"
