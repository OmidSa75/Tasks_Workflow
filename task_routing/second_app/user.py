from celery import shared_task


@shared_task(name='register_user')
def register_user(name: str) -> str:
    print(f"User {name} added")
    return "register_user"
