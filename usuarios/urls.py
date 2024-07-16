from rest_framework.routers import DefaultRouter
from .views import UserView, LoginView
from django.urls import path

router = DefaultRouter()
router.register(r"usuarios", UserView, basename="usuario")


#cuando es APIVIEW agregamos aqui
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns += router.urls