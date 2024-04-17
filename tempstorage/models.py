from django.db import models

# Create your models here.
class TempStorage(models.Model):
    data = models.JSONField()
