from django.shortcuts import render

from rest_framework import viewsets
from .serializers import taskSerializer, subTaskSerializer
from .models import task, subTask


class taskView(viewsets.ModelViewSet):
    serializer_class = taskSerializer
    queryset = task.objects.all()


class subTaskView(viewsets.ModelViewSet):
    serializer_class = subTaskSerializer
    queryset = subTask.objects.all()
