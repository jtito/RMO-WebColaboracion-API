from .models import DetailPermission
from scenarios.models import Scenario
from permissions.models import Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def insert_detalle_permisos(sender, **kwargs):
    if sender.name == "scenario_permissions":
        print("Migrando escenario x permiso")
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
            try:
                escenario_instance = Scenario.objects.get(pk=escenario_id)
                permission_instance = Permission.objects.get(pk=permission_id)
                detalle_permiso, created = DetailPermission.objects.get_or_create(
                    id=detalle_id,
                    escenario_id=escenario_instance,
                    permission_id=permission_instance,
                )
                
            except Scenario.DoesNotExist:
                print(f"Escenario con id {escenario_id} no existe.")
            except Permission.DoesNotExist:
                print(f"Permiso con id {permission_id} no existe.")
