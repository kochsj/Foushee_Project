from django.urls import path
from .views import newsfeed_view

urlpatterns = [
    path('newsfeed/', newsfeed_view, name='newsfeed')
]