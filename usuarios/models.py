from django.db import models

# Create your models here.


class Usuario(models.Model):
    TIPODOC_CHOICES = [
        ("DNI", "DNI"),
        ("CARNET", "Carnet de extranjeria"),
        ("PASSPORT", "Pasaporte"),
    ]
    ROLE_CHOICES = [
        ("ADMINISTRADOR", "Administrador"),
        ("SECRETARIA", "Secretaria"),
        ("PAIS", "País"),
        ("ENTIDAD", "Entidad"),
        ("AREA", "Área"),
    ]
    rol = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        null=False,
        blank=False,
        default="ADMINISTRADOR",
    )
    name = models.CharField(max_length=255, blank=False, null=False)
    last_nameF = models.CharField(max_length=255, blank=False, null=False)
    last_nameS = models.CharField(max_length=255, blank=False, null=False)
    tipo_doc = models.CharField(
        max_length=50,
        choices=TIPODOC_CHOICES,
        null=False,
        blank=False,
        default="DNI",
    )
    num_doc = models.CharField(
        max_length=25, blank=False, null=False, default="77777777", unique=True
    )
    email = models.CharField(
        max_length=255, blank=False, null=False, default="ejemplo@gmail.com"
    )
    password = models.CharField(
        max_length=255, blank=False, null=False, default="12345678"
    )
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name + " " + self.last_nameF + " " + self.last_nameS

    class Meta:
        db_table = "usuario"
