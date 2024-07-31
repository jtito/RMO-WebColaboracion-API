from django.test import TestCase
from perfil.models import Perfil
from scenario_permissions.models import DetailPermission
from scenarios.models import Scenario
from permissions.models import Permission
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from perfil.serializers import PerfilSerializer, PerfilSimpleSerializer

# Create your tests here.

class PerfilModelTest(TestCase):

    def setUp(self):
        self.scenario = Scenario.objects.create(id=1000, description='Test Scenario')
        self.permission = Permission.objects.create(id=1000, description='Test Permission')

        self.permission1 = DetailPermission.objects.create(
            id=1000,
            escenario_id=self.scenario,
            permission_id=self.permission
        )
        self.permission2 = DetailPermission.objects.create(
            id=1001,
            escenario_id=self.scenario,
            permission_id=self.permission
        )
        self.perfil = Perfil.objects.create(
            id=1000,
            description='Test Perfil'
        )
        self.perfil.detail_permisos.set([self.permission1, self.permission2])

    def test_perfil_creation(self):
        self.assertEqual(self.perfil.description, 'Test Perfil')
        self.assertEqual(self.perfil.detail_permisos.count(), 2)
        self.assertIn(self.permission1, self.perfil.detail_permisos.all())
        self.assertIn(self.permission2, self.perfil.detail_permisos.all())

class PerfilSerializerTest(TestCase):

    def setUp(self):
        self.scenario = Scenario.objects.create(id=2000, description='Test Scenario')
        self.permission = Permission.objects.create(id=2000, description='Test Permission')

        self.permission1 = DetailPermission.objects.create(
            id=2000,
            escenario_id=self.scenario,
            permission_id=self.permission
        )
        self.permission2 = DetailPermission.objects.create(
            id=2001,
            escenario_id=self.scenario,
            permission_id=self.permission
        )
        self.perfil = Perfil.objects.create(
            id=2000,
            description='Test Perfil'
        )
        self.perfil.detail_permisos.set([self.permission1, self.permission2])

    def test_perfil_serializer(self):
        serializer = PerfilSerializer(self.perfil)
        self.assertEqual(serializer.data['description'], 'Test Perfil')
        self.assertEqual(len(serializer.data['detail_permisos']), 2)

    def test_perfil_simple_serializer(self):
        serializer = PerfilSimpleSerializer(self.perfil)
        self.assertEqual(serializer.data['description'], 'Test Perfil')

class PerfilViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.scenario = Scenario.objects.create(id=3000, description='Test Scenario')
        self.permission = Permission.objects.create(id=3000, description='Test Permission')

        self.permission1 = DetailPermission.objects.create(
            id=3000,
            escenario_id=self.scenario,
            permission_id=self.permission
        )
        self.permission2 = DetailPermission.objects.create(
            id=3001,
            escenario_id=self.scenario,
            permission_id=self.permission
        )
        self.perfil = Perfil.objects.create(
            id=3000,
            description='Test Perfil'
        )
        self.perfil.detail_permisos.set([self.permission1, self.permission2])
        self.url = reverse('perfiles-list')

    def test_list_perfiles(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        perfil_data = next(perfil for perfil in response.data if perfil['id'] == 3000)
        self.assertEqual(perfil_data['description'], 'Test Perfil')

    def test_list_simple_perfiles(self):
        response = self.client.get(reverse('perfiles-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)