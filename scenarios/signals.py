from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Scenario

@receiver(post_migrate)
def insert_escenarios(sender, **kwargs):
    if sender.name == 'scenarios': 
        escenario = [
            (1, 'País'),
            (2, 'Comité'),
        ]
        for doc_id, description in escenario:
            Scenario.objects.get_or_create(id=doc_id, defaults={'description': description})
