from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://localhost",
    include=["app.tasks.tasks"]
)

# run celery
# celery -A app.tasks.celery_con:celery worker --loglevel=INFO --pool=solo
# celery -A app.tasks.celery_con:celery worker --loglevel=INFO --pool=solo
