from django.db import models

MAX_STRING_LENGTH = 80
MAX_IP_ADDRESS = 16

class Account(models.Model):
    username = models.CharField(max_length=MAX_STRING_LENGTH)
    password = models.CharField(max_length=MAX_STRING_LENGTH)
    email = models.IntegerField()
    balance = models.FloatField()

class Login(models.Model):
    username = models.CharField(max_length=MAX_STRING_LENGTH)
    ip_address = models.CharField(max_length=MAX_IP_ADDRESS)
    timestamp = models.TimeField()
    success = models.BooleanField()