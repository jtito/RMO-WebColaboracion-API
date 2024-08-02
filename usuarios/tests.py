from django.test import TestCase
from usuarios.models import Role, Usuario, PasswordResetToken
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.hashers import make_password

class PasswordResetTokenModelTest(TestCase):

    def setUp(self):
        self.role = Role.objects.create(id=200, description="Test Role")
        self.usuario = Usuario.objects.create(
            id=1,
            role=self.role,
            name="Test",
            last_nameF="User",
            last_nameS="Example",
            country="1",
            type_doc="1",
            doc_num="12345678",
            email="testuser@example.com",
            password=make_password("password")
        )

    def test_token_creation(self):
        token = PasswordResetToken.objects.create(user=self.usuario)
        self.assertIsNotNone(token.token)
        self.assertFalse(token.is_expired())


class UsuarioModelTest(TestCase):

    def setUp(self):
        self.role = Role.objects.create(id=201, description="Test Role")
        self.usuario1 = Usuario.objects.create(
            id=2,
            role=self.role,
            name="Test",
            last_nameF="User",
            last_nameS="Example",
            country="1",
            type_doc="1",
            doc_num="87654321",
            email="testuser2@example.com",
            password=make_password("password")
        )
        self.usuario2 = Usuario.objects.create(
            id=3,
            role=self.role,
            name="Another",
            last_nameF="Test",
            last_nameS="User",
            country="2",
            type_doc="2",
            doc_num="123456789",
            email="testuser3@example.com",
            password=make_password("password")
        )

    def test_usuario_country_display(self):
        usuario = Usuario.objects.get(id=2)
        self.assertEqual(usuario.get_country_display(), "Bolivia")

    def test_usuario_creation(self):
        Usuario.objects.create(
            id=4,
            role=self.role,
            name="AnotherTest",
            last_nameF="User",
            last_nameS="Example",
            country="3",
            type_doc="3",
            doc_num="123456700",
            email="testuser4@example.com",
            password=make_password("password")
        )
        self.assertEqual(Usuario.objects.count(), 3)

    def test_usuario_type_doc_display(self):
        usuario = Usuario.objects.get(id=2)
        self.assertEqual(usuario.get_type_doc_display(), "DNI")


class UsuarioViewTest(TestCase):

    def setUp(self):
        self.role = Role.objects.create(id=202, description="Test Role")
        self.client = APIClient()
        self.usuario = Usuario.objects.create(
            id=4,
            role=self.role,
            name="View",
            last_nameF="Test",
            last_nameS="User",
            country="3",
            type_doc="3",
            doc_num="23456789",
            email="testuser4@example.com",
            password=make_password("password")
        )

    def test_country_choices_view(self):
        response = self.client.get(reverse('country-choices'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'email': 'testuser4@example.com', 'password': 'password'})
        self.assertIn(response.status_code, [200, 400])

    def test_password_reset_request_view(self):
        response = self.client.post(reverse('password_reset_request'), {'email': 'testuser4@example.com'})
        self.assertEqual(response.status_code, 200)

    def test_password_reset_view(self):
        token = PasswordResetToken.objects.create(user=self.usuario)
        response = self.client.post(reverse('password_reset'), {'email': self.usuario.email, 'token': token.token, 'new_password': 'newpassword'})
        self.assertEqual(response.status_code, 200)

    def test_type_doc_choices_view(self):
        response = self.client.get(reverse('typedocs-choices'))
        self.assertEqual(response.status_code, 200)

    def test_usuario_create_view(self):
        response = self.client.post(reverse('usuario-list'), {
            'role': self.role.id,
            'name': 'Create',
            'last_nameF': 'Test',
            'last_nameS': 'User',
            'country': '1',
            'type_doc': '1',
            'doc_num': '34567890',
            'email': 'newuser@example.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 201)

    def test_usuario_delete_view(self):
        usuario = Usuario.objects.create(
            id=5,
            role=self.role,
            name="Delete",
            last_nameF="Test",
            last_nameS="User",
            country="1",
            type_doc="1",
            doc_num="45678901",
            email="deleteuser@example.com",
            password=make_password("password")
        )
        response = self.client.delete(reverse('usuario-detail', args=[usuario.id]))
        self.assertEqual(response.status_code, 204)

    def test_usuario_detail_view(self):
        response = self.client.get(reverse('usuario-detail', args=[self.usuario.id]))
        self.assertEqual(response.status_code, 200)

    def test_usuario_list_view(self):
        response = self.client.get(reverse('usuario-list'))
        self.assertEqual(response.status_code, 200)

    def test_usuario_update_view(self):
        usuario = Usuario.objects.create(
            id=6,
            role=self.role,
            name="Update",
            last_nameF="Test",
            last_nameS="User",
            country="1",
            type_doc="1",
            doc_num="56789012",
            email="updateuser@example.com",
            password=make_password("password")
        )
        response = self.client.put(reverse('usuario-detail', args=[usuario.id]), {
            'role': self.role.id,
            'name': 'Updated',
            'last_nameF': 'Test',
            'last_nameS': 'User',
            'country': '2',
            'type_doc': '2',
            'doc_num': '67890123',
            'email': 'updateduser@example.com',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 200)