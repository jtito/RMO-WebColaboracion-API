from django.test import TestCase
from django.db import connection
from django.db.models.signals import post_migrate
from .models import DetailPermission
from .signals import insert_detalle_permisos
from django.core.management import call_command


class ScenarioPermissionsSignalTestCase(TestCase):
    def setUp(self):
        pass

    def test_insert_detalle_permisos(self):
        call_command('migrate')
        expected_details = [
            (1, 1, 1),
            (2, 1, 2),
            (3, 1, 3),
            (4, 1, 4),
            (5, 1, 5),
            (6, 1, 6),
            (7, 2, 1),
            (8, 2, 2),
            (9, 2, 3),
            (10, 2, 4),
            (11, 2, 5),
            (12, 2, 6),
        ]
        for id, scenario_id, permission_id in expected_details:
            self.assertTrue(DetailPermission.objects.filter(id=id, escenario_id=scenario_id,permission_id=permission_id))
