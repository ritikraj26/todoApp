from rest_framework import serializers
from .models import task, subTask


class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ('id', 'title', 'deadline', 'completed')


class subTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = subTask
        fields = ('id', 'title', 'task', 'deadline', 'completed')

