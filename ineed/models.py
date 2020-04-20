from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(max_length=100, default='')
    phonenum = models.CharField(max_length=15, default='')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    myImage = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comcomment = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, blank=True)
    comauthor = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # manually deactivate inappropriate comments from admin site
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.comauthor)
