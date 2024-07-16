from rest_framework.routers import DefaultRouter
from .views import UserView, LoginView, CountryChoicesView,RoleChoicesView,TypeDocChoicesView
from django.urls import path

router = DefaultRouter()
router.register(r"usuarios", UserView, basename="usuario")


custom_urlpatterns = [
    path("role/",RoleChoicesView.as_view(),name="role-choices"),
    path("countries/",CountryChoicesView.as_view(),name="country-choices"),
    path("typedocs/",TypeDocChoicesView.as_view(),name="typedocs-choices"),
]


#cuando es APIVIEW agregamos aqui
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]+ custom_urlpatterns

urlpatterns += router.urls