from django.db import models
from tickets.models import Tickets


class Order(models.Model):
    ticket = models.ManyToManyField(Tickets, related_name='order')
