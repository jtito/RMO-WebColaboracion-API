from django.contrib import admin
from .models import Usuario
# Register your models here.


class UsuariosAdmin(admin.ModelAdmin):
    list_display = ["id","rol", "name", "last_nameF","last_nameS","tipo_doc","num_doc","is_active"]



admin.site.register(Usuario,UsuariosAdmin)
