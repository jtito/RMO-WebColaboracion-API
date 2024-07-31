from django.test import TestCase
from usuarios.models import Usuario
from role.models import Role

class UsuarioModelTest(TestCase):

    def setUp(self):
        self.role, created = Role.objects.get_or_create(
            id=100,
            defaults={'description': 'Test Role'}
        )
        self.usuario = Usuario.objects.create(
            role=self.role,
            name='John',
            last_nameF='Doe',
            last_nameS='Smith',
            country=1,
            type_doc=1,
            doc_num='12345678',
            email='john.doe@example.com',
            password='password'
        )

    def test_usuario_creation(self):
        self.assertEqual(self.usuario.name, 'John')
        self.assertEqual(self.usuario.last_nameF, 'Doe')
        self.assertEqual(self.usuario.last_nameS, 'Smith')
        self.assertEqual(self.usuario.get_country_display(), 'Bolivia')
        self.assertEqual(self.usuario.get_type_doc_display(), 'DNI')
        self.assertTrue(self.usuario.is_active)

    def test_get_country_display(self):
        self.assertEqual(self.usuario.get_country_display(), 'Bolivia')

    def test_get_type_doc_display(self):
        self.assertEqual(self.usuario.get_type_doc_display(), 'DNI')
