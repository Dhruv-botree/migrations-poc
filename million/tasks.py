from celery import shared_task
from .models import Million

@shared_task
def add_row(i):
    m = Million.objects.create(**{"dump":f"dump____{i}"})
    print(m.id)