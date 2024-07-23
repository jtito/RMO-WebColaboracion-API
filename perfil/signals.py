from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Perfil
from permissions.models import DetailPermission


@receiver(post_migrate)
def insert_perfil(sender, **kwargs):
    perfiles = []
    print("Migrando perfil y permisos")
    if sender.name == "perfil":
        perfiles = [
            (1, "Entidad", [1, 5, 6, 7, 11, 12]),
            (2, "Área", [6, 12]),
        ]
    for perfil_id, description, *permissions in perfiles:
        perfil, created = Perfil.objects.get_or_create(
            id=perfil_id, defaults={"description": description}
        )
        if created and permissions:
            permission_objs = DetailPermission.objects.filter(id__in=permissions)
            perfil.detail_permisos.set(permission_objs)
            perfil.save()
