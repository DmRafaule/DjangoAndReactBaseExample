from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AppModelSerializer
from .models import AppModel

class AppModelView(viewsets.ModelViewSet):
    serializer_class = AppModelSerializer
    queryset = AppModel.objects.all()
