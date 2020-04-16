from django.urls import path
from .views import employee_profile_view, settings_view

urlpatterns = [
    path('profile/', employee_profile_view, name='profile'),
    path('settings/', settings_view, name='settings'),
]