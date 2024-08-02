from django.test import TestCase
from role.models import Role
from scenario_permissions.models import DetailPermission
from documents.models import Document, Perfil, PerfilDocument, StateDocument, TypeDocument
from scenarios.models import Scenario
from permissions.models import Permission
from usuarios.models import Usuario
from rest_framework import status
from rest_framework.test import APITestCase

class DocumentModelTest(TestCase):
    def setUp(self):
        Role.objects.all().delete()
        DetailPermission.objects.all().delete()
        Perfil.objects.all().delete()
        Document.objects.all().delete()
        Scenario.objects.all().delete()
        Permission.objects.all().delete()
        Usuario.objects.all().delete()
        TypeDocument.objects.all().delete()
        StateDocument.objects.all().delete()

        self.scenario = Scenario.objects.create(id=100, description="Test Scenario")
        self.permission = Permission.objects.create(id=100, description="Test Permission")
        self.detail_permission = DetailPermission.objects.create(id=100, escenario_id=self.scenario, permission_id=self.permission)
        self.role = Role.objects.create(id=100, description="Admin Role")
        self.role.detail_permisos.add(self.detail_permission)
        self.perfil = Perfil.objects.create(id=100, description="Admin")
        self.usuario = Usuario.objects.create(id=100, role=self.role, name="John", last_nameF="Doe", last_nameS="Smith", country="US", type_doc="ID", doc_num="123456789", email="john.doe@example.com", password="securepassword")
        self.type_document = TypeDocument.objects.create(id=100, description="Test Type")
        self.state_document = StateDocument.objects.create(id=100, description="Test State")
        self.perfil_document = PerfilDocument.objects.create(user=self.usuario, perfil=self.perfil)
        self.document = Document.objects.create(id=100, typeDoc=self.type_document, usuario_creador=self.usuario, title="New Test Document", description="New Test Description", contenido="New Test Content", state=self.state_document)
        self.document.user_perfil.set([self.perfil_document])

    def test_document_creation(self):
        self.assertEqual(Document.objects.count(), 1)
        self.assertEqual(Document.objects.get(id=100).title, "New Test Document")

class DocumentViewSetTest(APITestCase):
    def setUp(self):
        # Limpia las instancias previas
        Role.objects.all().delete()
        DetailPermission.objects.all().delete()
        Perfil.objects.all().delete()
        Document.objects.all().delete()
        Scenario.objects.all().delete()
        Permission.objects.all().delete()
        Usuario.objects.all().delete()
        TypeDocument.objects.all().delete()
        StateDocument.objects.all().delete()

        # Crea las instancias necesarias
        self.scenario = Scenario.objects.create(id=100, description="Test Scenario")
        self.permission = Permission.objects.create(id=100, description="Test Permission")
        self.detail_permission = DetailPermission.objects.create(id=100, escenario_id=self.scenario, permission_id=self.permission)
        self.role = Role.objects.create(id=100, description="Admin Role")
        self.role.detail_permisos.add(self.detail_permission)
        self.perfil = Perfil.objects.create(id=100, description="Admin")
        self.usuario = Usuario.objects.create(id=100, role=self.role, name="John", last_nameF="Doe", last_nameS="Smith", country="US", type_doc="ID", doc_num="123456789", email="john.doe@example.com", password="securepassword")
        self.type_document = TypeDocument.objects.create(id=100, description="Test Type")
        self.state_document = StateDocument.objects.create(id=100, description="Test State")
        self.perfil_document = PerfilDocument.objects.create(user=self.usuario, perfil=self.perfil)
        self.document = Document.objects.create(id=100, typeDoc=self.type_document, usuario_creador=self.usuario, title="New Test Document", description="New Test Description", contenido="New Test Content", state=self.state_document)
        self.document.user_perfil.set([self.perfil_document])

    def test_get_documents(self):
        url = "/docs/docs/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Document.objects.count())
        self.assertEqual(response.data[0]['title'], 'New Test Document')

    def test_create_document(self):
        url = "/docs/docs/"
        data = {
            'typeDoc': self.type_document.id,
            'usuario_creador': self.usuario.id,
            'title': 'New Test Document',
            'description': 'New Test Description',
            'contenido': 'New Test Content',
            'state': self.state_document.id,
            'user_perfil': [self.perfil_document.id]
        }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_document = Document.objects.latest('id')
        print(f"Created document title: {created_document.title}")
        self.assertEqual(created_document.title, 'New Test Document')
        self.assertEqual(Document.objects.count(), 2)

class TypeDocumentViewSetTest(APITestCase):
    def setUp(self):
        self.type_document = TypeDocument.objects.create(id=200, description="Test Type")

    def test_get_type_documents(self):
        url = "/docs/tipo/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), TypeDocument.objects.count())


class PerfilxDocsViewSetTest(APITestCase):
    def setUp(self):
        self.scenario = Scenario.objects.create(id=300, description="Test Scenario")
        self.permission = Permission.objects.create(id=300, description="Test Permission")
        self.detail_permission = DetailPermission.objects.create(id=300, escenario_id=self.scenario, permission_id=self.permission)
        self.role = Role.objects.create(id=300, description="Admin Role")
        self.role.detail_permisos.add(self.detail_permission)
        self.perfil = Perfil.objects.create(id=300, description="Admin")
        self.usuario = Usuario.objects.create(id=300, role=self.role, name="John", last_nameF="Doe", last_nameS="Smith", country="US", type_doc="ID", doc_num="123456789", email="john.doe@example.com", password="securepassword")
        self.perfil_document = PerfilDocument.objects.create(id=300, user=self.usuario, perfil=self.perfil)

    def test_get_perfil_docs(self):
        url = "/docs/perfil/user/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), PerfilDocument.objects.count())
        self.assertEqual(response.data[0]['user']['name'], self.usuario.name)
        self.assertEqual(response.data[0]['user']['last_nameF'], self.usuario.last_nameF)
        self.assertEqual(response.data[0]['user']['last_nameS'], self.usuario.last_nameS)


class StateViewSetTest(APITestCase):
    def setUp(self):
        self.state_document = StateDocument.objects.create(id=400, description="Test State")

    def test_get_states(self):
        url = "/docs/state/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), StateDocument.objects.count())
