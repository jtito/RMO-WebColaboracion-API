from django.db import models
from usuarios.models import Usuario
from perfil.models import Perfil
# Create your models here.


class StateDocument(models.Model):
    description = models.CharField(max_length=80)
    class Meta:
        db_table ="state_doc"
    def __str__(self):
        return self.description

class PerfilDocument(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user} - {self.perfil}"

    class Meta:
        db_table = "perfil_doc"



class TypeDocument(models.Model):

    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    def __str__(self):
        return self.description
    class Meta:
        db_table = "typeDoc"

class Document(models.Model):
    typeDoc = models.ForeignKey(TypeDocument,on_delete=models.CASCADE)
    usuario_creador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True) #JALA DE USUARIO LOGUEADO 
    title = models.TextField(max_length=200, null=True)
    description = models.TextField(null=True)
    user_perfil = models.ManyToManyField(
        PerfilDocument, related_name="perfilxdocumento", null=True, blank=True
    )
    state = models.ForeignKey(StateDocument, default=1, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    change_state = models.DateField(null=True)
    def __str__(self):
        return self.description

    class Meta:
        db_table = "documents"



