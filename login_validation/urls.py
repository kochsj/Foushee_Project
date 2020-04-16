from django.urls import path
from .views import login_validation_view

urlpatterns = [
    path('login/', login_validation_view, name='login')
]