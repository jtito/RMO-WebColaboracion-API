from django.db import models
from role.models import Role
from django.utils import timezone
import random
# Create your models here.


class Usuario(models.Model):

    COUNTRIES_CHOICES = [
        (1, "Bolivia"),
        (2, "Colombia"),
        (3, "Ecuador"),
        (4, "Perú"),
    ]

    TYPEDOC_CHOICES = [
        (1, "Cédula de Identidad"),
        (2, "Carnet de extranjeria"),
        (3, "Pasaporte"),
    ]
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=4)  
    name = models.CharField(max_length=255, blank=False, null=False)
    last_nameF = models.CharField(max_length=255, blank=False, null=False)
    last_nameS = models.CharField(max_length=255, blank=False, null=False)
    country = models.CharField(
        max_length=50,
        choices=COUNTRIES_CHOICES,
        null=False,
        blank=False,
        default=1,
    )
    type_doc = models.CharField(
        max_length=50,
        choices=TYPEDOC_CHOICES,
        null=False,
        blank=False,
        default=1,
    )
    doc_num = models.CharField(
        max_length=25, blank=False, null=False, default="77777777", unique=True
    )
    email = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        default="ejemplo@gmail.com",
        unique=True,
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

    @staticmethod
    def get_country_choices():
        return Usuario.COUNTRIES_CHOICES

    @staticmethod
    def get_type_doc_choices():
        return Usuario.TYPEDOC_CHOICES


    def get_country_display(self):
        return dict(self.COUNTRIES_CHOICES).get(int(self.country))

    def get_type_doc_display(self):
        return dict(self.TYPEDOC_CHOICES).get(int(self.type_doc))

class PasswordResetToken(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    token = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = str(random.randint(100000, 999999))  # Token de 6 dígitos
        if not self.expires_at:
            self.expires_at = timezone.now() + timezone.timedelta(hours=1)
        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"{self.user.email} - {self.token}"