from django.db import models

# Create your models here.


# Create your models here.
from django.contrib.auth.models import User


class Account(models.Model):
    choices = [
        ('admin', 'Admin'),
        ('employee', 'Employee'),
        ('client', 'Client'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone_no = models.CharField(max_length=15)