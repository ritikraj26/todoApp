from django.db import models

class task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    deadline = models.TimeField(auto_now=True)
    subTask = models.ForeignKey(subTask, on_delete=models.CASCADE())

class subTask(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    deadline = models.TimeField(auto_now=True)
