from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(max_length=100, default='')
    age = models.IntegerField(default=0)
    phonenum = models.CharField(max_length=15, default='')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    myImage = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name
