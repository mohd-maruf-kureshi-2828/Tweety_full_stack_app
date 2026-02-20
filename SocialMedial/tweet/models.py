from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    text=models.TextField(max_length=280)
    photo = models.ImageField(upload_to='tweets/photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    likes = models.ManyToManyField(
        User,
        related_name='liked_tweets',
        blank=True
          )

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'Tweet by {self.user.username} at {self.text[:20]}'
    
class Comment(models.Model):
    tweet = models.ForeignKey(
        Tweet,
        related_name='comments',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username}'
