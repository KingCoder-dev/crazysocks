from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Polls (models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    liked = models.ManyToManyField(User, default=None, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    @property
    def num_likes(self):
        return self.liked.all().count()


LIKE_CHOICES = (
    ('like', 'like'),
    ('unlike', 'unlike')
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    polls = models.ForeignKey(Polls, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,
                             default='like', max_length=10)

    def __str__(self):
        return str(self.post)
