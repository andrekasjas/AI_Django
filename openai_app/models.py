from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=1000)
    sender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)