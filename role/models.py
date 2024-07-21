from django.db import models
from permissions.models import DetailPermissionDocs


class Role(models.Model):
    ROLE_CHOICES = [
        (1, "Administrador del sistema"),
        (2, "Secretaria Técnica (SGCAN)"),
        (3, "País Miembro (PPMM)"),
        (4, "Entidad"),
        (5, "Área"),
    ]
    description = models.IntegerField(
        choices=ROLE_CHOICES,
        null=False,
        blank=False,
        default=1,
    )
    detail_permisos = models.ManyToManyField(DetailPermissionDocs, blank=False)

    def __str__(self) -> str:
        return dict(self.ROLE_CHOICES).get(self.description, "Unknown Role")
