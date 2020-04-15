from django.urls import path
from .views import LoginValidationView

urlpatterns = [
    path('login/', LoginValidationView.as_view(), name='login')
]