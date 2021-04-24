from django.db import models


class Tweet(models.Model):
    text = models.TextField()
    photo = models.URLField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'Tweet: ({self.author.username}, {self.text[:20]})'

class Follow(models.Model):
    follows = models.ForeignKey('auth.User', related_name='follower', on_delete=models.CASCADE)
    follower = models.ForeignKey('auth.User', related_name='follows', on_delete=models.CASCADE)
    followed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Follow: {self.follower.username} -> {self.follows.username}'