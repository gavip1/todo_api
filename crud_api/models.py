from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Meta:
        ordering = ['date_joined']
    pass

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')
    title = models.CharField(max_length=100, blank=True)
    task_detail = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True)
    date_finished = models.DateTimeField(blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_created']