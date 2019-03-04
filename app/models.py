from django.db import models

# Create your models here.
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=50)