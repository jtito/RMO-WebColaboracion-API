from django.test import TestCase
from role.models import Role
from scenario_permissions.models import DetailPermission
from scenarios.models import Scenario
from permissions.models import Permission
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from role.serializers import RoleSerializer, RoleSimpleSerializer

class RoleModelTest(TestCase):

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
        self.role = Role.objects.create(
            id=1000, 
            description='Test Role'
        )
        self.role.detail_permisos.set([self.permission1, self.permission2])

    def test_role_creation(self):
        self.assertEqual(self.role.description, 'Test Role')
        self.assertEqual(self.role.detail_permisos.count(), 2)
        self.assertIn(self.permission1, self.role.detail_permisos.all())
        self.assertIn(self.permission2, self.role.detail_permisos.all())

class RoleSerializerTest(TestCase):

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
        self.role = Role.objects.create(
            id=2000, 
            description='Test Role'
        )
        self.role.detail_permisos.set([self.permission1, self.permission2])

    def test_role_serializer(self):
        serializer = RoleSerializer(self.role)
        self.assertEqual(serializer.data['description'], 'Test Role')
        self.assertEqual(len(serializer.data['detail_permisos']), 2)

    def test_role_simple_serializer(self):
        serializer = RoleSimpleSerializer(self.role)
        self.assertEqual(serializer.data['description'], 'Test Role')

class RoleViewTest(TestCase):

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
        self.role = Role.objects.create(
            id=3000, 
            description='Test Role'
        )
        self.role.detail_permisos.set([self.permission1, self.permission2])
        self.url = reverse('roles-list')

    def test_list_roles(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        role_data = next(role for role in response.data if role['id'] == 3000)
        self.assertEqual(role_data['description'], 'Test Role')

    def test_list_simple_roles(self):
        response = self.client.get(reverse('roles-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)