from django.db import models
from permissions.models import DetailPermission


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(
        max_length=100,
    )
    detail_permisos = models.ManyToManyField(
        DetailPermission
    )

    def __str__(self) -> str:
        return self.description

    class Meta:
        db_table = "role"

