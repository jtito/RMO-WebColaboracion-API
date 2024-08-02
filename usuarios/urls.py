from rest_framework.routers import DefaultRouter
from .views import UserView, LoginView, CountryChoicesView, TypeDocChoicesView, PasswordResetRequestView, PasswordResetView
from django.urls import path

router = DefaultRouter()
router.register(r'usuarios', UserView, basename='usuario')

custom_urlpatterns = [
    path('countries/', CountryChoicesView.as_view(), name='country-choices'),
    path('typedocs/', TypeDocChoicesView.as_view(), name='typedocs-choices'),
]

urlpatterns = [
    path('password-reset-request/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('login/', LoginView.as_view(), name='login'),
] + custom_urlpatterns

urlpatterns += router.urls