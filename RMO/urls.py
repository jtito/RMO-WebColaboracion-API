from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Django API",
        default_version="v1",
        description="API Codigo Backend",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ani.rojas.sen@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("usuarios.urls")),
    path(
        "swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-api"
    ),
    path("docs/", include("documents.urls")),
    path("escenario/",include("scenarios.urls")),
    path("permisos/", include("permissions.urls")),
    path("roles/",include("role.urls")),
    path("perfil/",include("perfil.urls")),
    path("permisos/", include("scenario_permissions.urls")),
    path('usuarios/', include('usuarios.urls')),
]
