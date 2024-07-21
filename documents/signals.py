from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Document

@receiver(post_migrate)
def insert_documents(sender, **kwargs):
    if sender.name == 'documents': 
        documents = [
            (1, 'Desiciones'),
            (2, 'Resoluciones'),
            (3, 'Documentos Técnicos'),
        ]
        for doc_id, description in documents:
            Document.objects.get_or_create(id=doc_id, defaults={'description': description})
