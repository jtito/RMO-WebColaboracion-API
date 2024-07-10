from rest_framework.routers import DefaultRouter
from .views import UsuarioView, LoginView
from django.urls import path

router = DefaultRouter()
router.register(r"usuarios", UsuarioView, basename="usuario")


#cuando es APIVIEW agregamos aqui
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns += router.urls