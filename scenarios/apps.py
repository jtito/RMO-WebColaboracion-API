from django.apps import AppConfig


class ScenariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scenarios'
    def ready(self):
        import scenarios.signals