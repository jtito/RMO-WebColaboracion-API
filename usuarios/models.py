from django.db import models

# Create your models here.


class Usuario(models.Model):

    COUNTRIES_CHOICES = [
        ("BOLIVIA", "Bolivia"),
        ("COLOMBIA", "Colombia"),
        ("ECUADOR", "Ecuador"),
        ("PERÚ", "Perú"),
    ]

    TYPEDOC_CHOICES = [
        ("DNI", "DNI"),
        ("CARNET", "Carnet de extranjeria"),
        ("PASSPORT", "Pasaporte"),
    ]
    ROLE_CHOICES = [
        ("ADMINISTRADOR", "Administrador del sistema"),
        ("SECRETARIA ", "Secretaria Técnica (SGCAN)"),
        ("PAIS", "País Miembro (PPMM)"),
        ("ENTIDAD", "Entidad"),
        ("AREA", "Área"),
    ]
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        null=False,
        blank=False,
        default="ADMINISTRADOR",
    )
    name = models.CharField(max_length=255, blank=False, null=False)
    last_nameF = models.CharField(max_length=255, blank=False, null=False)
    last_nameS = models.CharField(max_length=255, blank=False, null=False)
    country = models.CharField(
        max_length=50,
        choices=COUNTRIES_CHOICES,
        null=False,
        blank=False,
        default="Perú"
    )
    type_doc = models.CharField(
        max_length=50,
        choices=TYPEDOC_CHOICES,
        null=False,
        blank=False,
        default="DNI",
    )
    doc_num = models.CharField(
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
