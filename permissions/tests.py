from django.test import TestCase
from django.db import connection
from django.db.models.signals import post_migrate
from .models import Permission
from .signals import insert_permissos
from django.core.management import call_command

class PermissionSignalTestCase(TestCase):
    def setUp(self):
        # Configuración previa si es necesario
        pass

    def test_insert_permissions_signal(self):
        # Ejecuta todas las migraciones
        call_command('migrate')

        # Verifica que los permisos esperados estén presentes en la base de datos
        expected_permissions = [
            (1, "Editar"),
            (2, "Crear"),
            (3, "Aprobar"),
            (4, "Archivar"),
            (5, "Votar"),
            (6, "Comentar"),
        ]
        for perm_id, description in expected_permissions:
            self.assertTrue(Permission.objects.filter(id=perm_id, description=description).exists())
