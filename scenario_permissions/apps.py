from django.apps import AppConfig


class ScenarioPermissionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scenario_permissions'
    def ready(self):
        import scenario_permissions.signals