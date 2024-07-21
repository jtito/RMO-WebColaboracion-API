from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Permission, DetailPermissionDocs
from scenarios.models import Scenario


@receiver(post_migrate)
def insert_permissos(sender, **kwargs):
    if sender.name == "Permissions":
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


@receiver(post_migrate)
def insert_detalle_permisos(sender, **kwargs):
    if sender.name == "Permissions":
        escenario_permisos = [
            (1,1, 1),
            (2,1, 2),
            (3,1, 3),
            (4,1, 4),
            (5,1, 5),
            (6,1, 6),
            (7,2, 1),
            (8,2, 2),
            (9,2, 3),
            (10,2, 4),
            (11,2, 5),
            (12,2, 6),
        ]
        for detalle_id,escenario_id, permission_id in escenario_permisos:
            escenario_instance = Scenario.objects.get(pk=escenario_id)
            permission_instance = Permission.objects.get(pk=permission_id)
            DetailPermissionDocs.objects.get_or_create(
                id=detalle_id,escenario_id=escenario_instance, permission_id=permission_instance
            )
