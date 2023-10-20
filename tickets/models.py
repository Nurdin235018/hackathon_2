from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
#verbose_name


class Category(models.Model):
    is_business = models.BooleanField(default=False)
    is_economy = models.BooleanField(default=True)
    is_first_class = models.BooleanField(default=False)


class Flight(models.Model):
    all_places = models.IntegerField()
    image = models.ImageField(upload_to='flights/', blank=True)
    description = models.TextField()
    where_from = models.CharField(max_length=40)
    where_to = models.CharField(max_length=40)
    time = models.IntegerField()


class Tickets(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='tickets', verbose_name='Airline')
    place = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tickets', verbose_name='Class')
    luggage = models.CharField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.id} {self.title}'
