from django.test import TestCase
from django.db import connection
from django.db.models.signals import post_migrate
from .models import Scenario
from .signals import insert_escenarios
from django.core.management import call_command

class ScenariosSignalTestCase(TestCase):
    def setUp(self):
        pass

    def test_insert_scenarios_signal(self):
        call_command('migrate')

        expected_scenarios =[
            (1, 'País'),
            (2, 'Comité'),
        ]
        for id, description in expected_scenarios:
            self.assertTrue(Scenario.objects.filter(id=id,description=description).exists())
