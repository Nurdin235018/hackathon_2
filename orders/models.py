from django.db import models
from tickets.models import Tickets


class Order(models.Model):
    email = models.EmailField(primary_key=True, unique=True)
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)



