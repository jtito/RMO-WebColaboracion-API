from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Role
from scenario_permissions.models import DetailPermission

@receiver(post_migrate)
def insert_roles(sender, **kwargs):
    print("Migrando roles y permisos")
    
    if sender.name == "role":
        print("Nombre de aplicación confirmado: ", sender.name)
        roles = [
            (1, "Administrador del sistema"),
            (2, "Secretaria Técnica (SGCAN)", [7, 8, 9, 10]),
            (3, "País Miembro (PPMM)", [1, 2, 3, 4, 7, 11, 12]),
            (4, "Ninguno"),
        ]
        
        for role_id, description, *permissions in roles:
            role, created = Role.objects.get_or_create(
                id=role_id, defaults={"description": description}
            )
            
            
            if permissions:
                permission_ids = permissions[0]  
                
                permission_objs = DetailPermission.objects.filter(id__in=permission_ids)
                
                role.detail_permisos.set(permission_objs)
                role.save()
            else:
                print(f"No se encontraron permisos para el rol {role_id}")
