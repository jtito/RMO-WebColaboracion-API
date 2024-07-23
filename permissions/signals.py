from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Permission, DetailPermission
from scenarios.models import Scenario


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


@receiver(post_migrate)
def insert_detalle_permisos(sender, **kwargs):
    print("Migrando escenario x permiso")
    if sender.name == "permissions":
        escenario_permisos = [
            (1, 1, 1),
            (2, 1, 2),
            (3, 1, 3),
            (4, 1, 4),
            (5, 1, 5),
            (6, 1, 6),
            (7, 2, 1),
            (8, 2, 2),
            (9, 2, 3),
            (10, 2, 4),
            (11, 2, 5),
            (12, 2, 6),
        ]
        for detalle_id, escenario_id, permission_id in escenario_permisos:
            print(f"Procesando detalle_id {detalle_id} - escenario_id {escenario_id} - permission_id {permission_id}")
            
            try:
                escenario_instance = Scenario.objects.get(pk=escenario_id)
                print(f"Escenario encontrado: {escenario_instance}")
            except Scenario.DoesNotExist:
                print(f"Escenario con id {escenario_id} no existe.")
                continue  

            try:
                permission_instance = Permission.objects.get(pk=permission_id)
                print(f"Permiso encontrado: {permission_instance}")
            except Permission.DoesNotExist:
                print(f"Permiso con id {permission_id} no existe.")
                continue  

            detalle_permiso, created = DetailPermission.objects.get_or_create(
                id=detalle_id,
                escenario_id=escenario_instance,
                permission_id=permission_instance,
            )
            
            if created:
                print(f"DetallePermission creado: {detalle_permiso}")
            else:
                print(f"DetallePermission ya existe: {detalle_permiso}")
