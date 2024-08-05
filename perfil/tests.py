from django.test import TestCase
from django.db.models.signals import post_migrate
from django.test.utils import override_settings
from django.core.management import call_command
from io import StringIO
from .models import Perfil
from .signals import insert_perfil
from .views import PerfilView
from rest_framework.test import APIRequestFactory
from scenario_permissions.models import DetailPermission
from scenarios.models import Scenario
from permissions.models import Permission

class PerfilModelTest(TestCase):

    def setUp(self):
        self.scenario = Scenario.objects.create(id=100, description='Scenario Test')
        self.permission = Permission.objects.create(id=100, description='Permission Test')
        self.detail_permission = DetailPermission.objects.create(id=100, escenario_id=self.scenario, permission_id=self.permission)

    def test_perfil_creation(self):
        perfil = Perfil.objects.create(id=100, description="Test Perfil")
        perfil.detail_permisos.add(self.detail_permission)
        self.assertEqual(perfil.description, "Test Perfil")
        self.assertIn(self.detail_permission, perfil.detail_permisos.all())

class PerfilViewTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.scenario = Scenario.objects.create(id=200, description='Scenario Test')
        self.permission = Permission.objects.create(id=200, description='Permission Test')
        self.detail_permission = DetailPermission.objects.create(id=200, escenario_id=self.scenario, permission_id=self.permission)
        self.perfil = Perfil.objects.create(id=200, description="Test Perfil")
        self.perfil.detail_permisos.add(self.detail_permission)

    def test_perfil_list_view(self):
        request = self.factory.get('/perfiles/')
        view = PerfilView.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(perfil['id'] == self.perfil.id for perfil in response.data))

    def test_perfil_detail_view(self):
        request = self.factory.get(f'/perfiles/{self.perfil.id}/')
        view = PerfilView.as_view({'get': 'retrieve'})
        response = view(request, pk=self.perfil.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['description'], self.perfil.description)

class PerfilSignalTest(TestCase):

    def setUp(self):
        Scenario.objects.create(id=300, description='Scenario Test')
        Permission.objects.create(id=300, description='Permission Test')
        DetailPermission.objects.create(id=300, escenario_id_id=300, permission_id_id=300)

    @override_settings(INSTALLED_APPS=['__main__'])
    def test_insert_perfil_signal(self):
        post_migrate.connect(insert_perfil, sender=self.__class__)
        out = StringIO()
        call_command('migrate', stdout=out)

        # Aca verificamos que los perfiles y permisos se hayan creado correctamente
        perfil_entidad = Perfil.objects.get(id=1)
        perfil_area = Perfil.objects.get(id=2)
        self.assertEqual(perfil_entidad.description, "Entidad")
        self.assertEqual(perfil_area.description, "Área")

        # Verificamos los permisos asociados
        self.assertEqual(list(perfil_entidad.detail_permisos.values_list('id', flat=True)), [1, 5, 6, 7, 11, 12])
        self.assertEqual(list(perfil_area.detail_permisos.values_list('id', flat=True)), [6, 12])