from django.contrib import admin
from .models import task, subTask

admin.site.register(task)
admin.site.register(subTask)
