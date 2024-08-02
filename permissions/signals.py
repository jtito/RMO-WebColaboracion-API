from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Permission



@receiver(post_migrate)
def insert_permissos(sender, **kwargs):
    if sender.name == "permissions":
        permissions = [
            (1, "Editar"),
            (2, "Crear"),
            (3, "Aprobar"),
            (4, "Archivar"),
            (5, "Votar"),
            (6, "Comentar"),
        ]
        for permissions_id, description in permissions:
            Permission.objects.get_or_create(
                id=permissions_id, defaults={"description": description}
            )



