from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.response import Response


User = get_user_model()
#verbose_name


class Category(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    place_class = models.CharField(max_length=20, primary_key=True)


class Flight(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    all_places = models.IntegerField()
    image = models.ImageField(upload_to='flights/', blank=True)
    description = models.TextField()
    where_from = models.CharField(max_length=40)
    where_to = models.CharField(max_length=40, primary_key=True)
    time = models.IntegerField()

    def decrease_total_ticket(self):
        if self.all_places > 0:
            self.all_places -= 1
            self.save(update_fields=['total_ticket'])

    def __str__(self):
        return f'{self.where_from}-{self.where_to}'


class Tickets(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='tickets', verbose_name='Airline')
    place = models.PositiveIntegerField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tickets', verbose_name='Class')
    luggage = models.CharField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def place_number(self):
        if self.place > self.flight.all_places:
            return Response('You can\'t take this place')
        return Response('You successfully got your ticket')

    def __str__(self):
        return f'{self.id} {self.title}'
