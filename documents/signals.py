from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import TypeDocument,StateDocument

@receiver(post_migrate)
def insert_documents(sender, **kwargs):
    if sender.name == 'documents': 
        documents = [
            (1, 'Desiciones'),
            (2, 'Resoluciones'),
            (3, 'Documentos Técnicos'),
        ]
        for doc_id, description in documents:
            TypeDocument.objects.get_or_create(id=doc_id, defaults={'description': description})



@receiver(post_migrate)
def insert_state_documents(sender,**kwargs):
    if sender.name =='documents':
        states = [
            (1,'Borrador'),
            (2,'Publicado'),
            (3,'Eliminado')
        ]
        for states_id, description in states:
            StateDocument.objects.get_or_create(id=states_id,defaults={'description': description})