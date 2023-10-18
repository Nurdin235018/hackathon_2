from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=40, unique=True)
    slug = models.CharField(max_length=40, primary_key=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


class Tag(models.Model):
    title = models.CharField(max_length=40, unique=True)
    slug = models.CharField(max_length=40, primary_key=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


class Tickets(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets', verbose_name='Author')
    body = models.TextField()
    where_from = models.CharField(max_length=40)
    where_to = models.CharField(max_length=40)
    image = models.ImageField(upload_to='tickets/', blank=True)
    tags = models.ManyToManyField(Tag, related_name='tickets', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tickets')
    price = models.IntegerField() #may be fail

    def __str__(self):
        return f'{self.id} {self.title}'
