from rest_framework.routers import DefaultRouter
from .views import RoleView,RoleChoicesView
from django.urls import path
router = DefaultRouter()
router.register(r"role", RoleView, basename="roles")


custom_urlpatterns = [
    path("choices-rol/",RoleChoicesView.as_view(),name="role-choices"),
]

urlpatterns = router.urls