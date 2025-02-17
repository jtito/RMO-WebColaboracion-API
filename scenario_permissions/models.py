from django.db import models
from scenarios.models import Scenario
from permissions.models import Permission
# Create your models here.


class DetailPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    escenario_id = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    permission_id = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.escenario_id} - {self.permission_id}"
    class Meta:
        db_table = "detail_permission"