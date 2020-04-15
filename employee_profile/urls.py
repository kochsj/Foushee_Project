from django.urls import path
from .views import EmployeeProfileView, SettingsView

urlpatterns = [
    path('profile/', EmployeeProfileView.as_view(), name='profile'),
    path('settings/', SettingsView.as_view(), name='settings'),
]