from django.urls import path, include
from .views import app_view

urlpatterns = [
    path('', app_view)
]
