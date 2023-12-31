from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

class TimelineEvent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.title