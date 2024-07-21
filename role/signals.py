from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Role
from permissions.models import DetailPermissionDocs

@receiver(post_migrate)
def insert_roles(sender, **kwargs):
    print("Post migrate signal triggered")
    if sender.name == "role":
        roles = [
            (1, "Administrador del sistema"),
            (2, "Secretaria Técnica (SGCAN)", [8, 7, 9, 10]),
            (3, "País Miembro (PPMM)", [11, 7, 12, 2, 1, 3, 4]),
            (4, "Entidad", [5, 7, 6]),
            (5, "Área", [6]),
        ]
        for roles_id, description, *permissions in roles:
            role, created = Role.objects.get_or_create(
                id=roles_id, defaults={"description": description}
            )
            if created and permissions:
                permission_objs = DetailPermissionDocs.objects.filter(id__in=permissions[0])
                role.detail_permisos.set(permission_objs)
                role.save()

