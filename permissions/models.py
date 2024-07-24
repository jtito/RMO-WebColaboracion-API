from django.db import models
from scenarios.models import Scenario

# Create your models here.

class Permission(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    class Meta:
        db_table = "permission"

class DetailPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    escenario_id = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    permission_id = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.escenario_id} - {self.permission_id}"
    class Meta:
        db_table = "detail_permission"