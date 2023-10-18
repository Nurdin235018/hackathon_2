from django.db import models
from account.admin import User
from tickets.models import Tickets


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Tickets, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.author.name} liked {self.ticket.title}'


class Rating(models.Model):
    rating = models.PositiveSmallIntegerField()
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name='ratings')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return f'{self.rating} - {self.ticket}'


class Favourites(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name='favourites')

    def __str__(self):
        return f'{self.author} {self.ticket}'

