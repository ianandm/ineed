from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phonenumber = models.CharField(max_length=15, default='')
    age = models.CharField(max_length=3)
    city = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.user.username} Profile'


