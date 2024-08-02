from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Role
from scenario_permissions.models import DetailPermission
from scenarios.models import Scenario
from permissions.models import Permission

class RoleModelTest(TestCase):

    def setUp(self):
        self.scenario = Scenario.objects.create(id=100, description="Test Scenario")
        self.permission = Permission.objects.create(id=100, description="Test Permission")
        self.detail_permission = DetailPermission.objects.create(
            id=100,
            escenario_id=self.scenario,
            permission_id=self.permission
        )
        self.role = Role.objects.create(
            id=100,
            description="Admin"
        )
        self.role.detail_permisos.add(self.detail_permission)

    def test_role_creation(self):
        self.assertTrue(isinstance(self.role, Role))
        self.assertEqual(self.role.__str__(), self.role.description)


class RoleViewTest(APITestCase):

    def setUp(self):
        self.scenario, _ = Scenario.objects.get_or_create(id=1, defaults={'description': "Test Scenario"})
        self.permission, _ = Permission.objects.get_or_create(id=1, defaults={'description': "Test Permission"})
        self.detail_permission, _ = DetailPermission.objects.get_or_create(
            id=1,
            defaults={
                'escenario_id': self.scenario,
                'permission_id': self.permission
            }
        )
        self.role, _ = Role.objects.get_or_create(
            id=100,
            defaults={'description': "Admin"}
        )
        self.role.detail_permisos.add(self.detail_permission)
        self.role_data = {
            'id': 200,
            'description': 'User',
            'detail_permisos': [self.detail_permission.id]
        }

    def test_role_list(self):
        response = self.client.get(reverse('roles-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_role_detail(self):
        response = self.client.get(reverse('roles-detail', kwargs={'pk': self.role.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RoleSignalTest(APITestCase):

    def test_insert_roles_signal(self):
        from django.db.models.signals import post_migrate
        from role.signals import insert_roles
        from django.apps import apps
        from io import StringIO

        # Prepara para la salida en memoria es decir en un buffer de memoria en lugar de la salida estándar
        out = StringIO()

        # Redirigir la salida estándar quiere decir que todo lo que se imprima en la consola se guardará en la variable out
        import sys
        sys.stdout = out

        try:
            # Disparar la señal post_migrate quiere decir que se ejecutarán las migraciones de la aplicación role y se insertarán los roles
            app_config = apps.get_app_config('role')
            post_migrate.send(sender=   app_config, app_config=app_config, verbosity=1, interactive=False)

            # Llamar al manejador de señales para insertar los roles y permisos en la base de datos
            insert_roles(app_config, verbosity=1, interactive=False)
        finally:
            # Restaurar la salida estándar es decir la consola
            sys.stdout = sys.__stdout__

        self.assertIn("Migrando roles y permisos", out.getvalue())
