from django.db import models
from permissions.models import DetailPermissionDocs


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(
        max_length=100,
    )
    detail_permisos = models.ManyToManyField(DetailPermissionDocs, blank=False)

    def __str__(self) -> str:
        return self.description
    
    class Meta:
        db_table = "role"

