from django.contrib import admin
from .models import Usuario
# Register your models here.


class UsuariosAdmin(admin.ModelAdmin):
    list_display = ["id","role", "name", "last_nameF","last_nameS","type_doc","doc_num","is_active"]



admin.site.register(Usuario,UsuariosAdmin)
