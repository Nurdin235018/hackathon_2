from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify


User = get_user_model()

class Ticket(models.Model):
    title = models.CharField(max_length=40)
    price = models.IntegerField()



class Category(models.Model):
    title = models.CharField(max_length=40, unique=True)
    slug = models.CharField(max_length=40, primary_key=True, blank=True)


