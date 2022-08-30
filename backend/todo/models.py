from django.db import models


class task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    deadline = models.TimeField()

    def __str__(self):
        return self.title

class subTask(models.Model):
    task = models.ForeignKey(task, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    deadline = models.TimeField()

    def __str__(self):
        return self.title