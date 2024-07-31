from django.db import models
from scenario_permissions.models import DetailPermission


# Create your models here.
class Perfil(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)
    detail_permisos = models.ManyToManyField(DetailPermission, blank=False)

    def __str__(self) -> str:
        return self.description

    class Meta:
        db_table = "perfil"
