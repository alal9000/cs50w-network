from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(blank=False,)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='like_user')

    def __str__(self):
        return self.post


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follower = models.ManyToManyField(User, blank=True, related_name='follower_user')
    following = models.ManyToManyField(User, blank=True, related_name='following_user')

    def __str__(self):
        return self.user.username







