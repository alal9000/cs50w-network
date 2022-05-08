from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    following = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(blank=False,)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='user_like')

    def __str__(self):
        return self.post







