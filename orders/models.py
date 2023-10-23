import django_extensions.templatetags.highlighting
from django.db import models
from tickets.models import Tickets
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string


User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    email = models.EmailField()
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name='order')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=False, help_text='Active')
    activation_code = models.CharField(max_length=40, blank=True, help_text='Orders\' code')

    def create_activation_code(self):
        code = get_random_string(10)
        self.activation_code = code
        self.save()

    def __str__(self):
        return f"Order {self.pk} by {self.user.name}"




