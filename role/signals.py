from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Role
from permissions.models import DetailPermission

@receiver(post_migrate)
def insert_roles(sender, **kwargs):
    if sender.name == "role":
        print("Migrando roles y permisos...")
        roles = [
            (1, "Administrador del sistema"),
            (2, "Secretaria Técnica (SGCAN)", [7, 8, 9, 10]),
            (3, "País Miembro (PPMM)", [1, 2, 3, 4, 7, 11, 12]),
        ]
        for role_id, description, *permissions in roles:
            print(f"Procesando rol {role_id} - {description}")
            role, created = Role.objects.get_or_create(
                id=role_id, defaults={"description": description}
            )
            if created:
                print(f"Rol creado: {role_id} - {description}")
            else:
                print(f"Rol ya existente: {role_id} - {description}")

            if permissions:
                permission_ids = permissions[0]  # Extrae la lista de permisos
                print(f"Permisos asociados: {permission_ids}")

                # Filtra permisos usando una lista de IDs
                permission_objs = DetailPermission.objects.filter(id__in=permission_ids)
                print(f"Permisos encontrados: {permission_objs}")

                # Asigna permisos al rol
                role.detail_permisos.set(permission_objs)
                role.save()
                print(f"Rol actualizado: {role_id}")
            else:
                print(f"No se encontraron permisos para el rol {role_id}")