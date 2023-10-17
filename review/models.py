from django.db import models
from account.admin import User
from tickets.models import Tickets


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Tickets, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.author.name} liked {self.post.title}'


class Rating(models.Model):
    rating = models.PositiveSmallIntegerField()
    post = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name='ratings')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return f'{self.rating} - {self.post}'

