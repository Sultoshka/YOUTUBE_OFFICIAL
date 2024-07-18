from django.db import models
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Video_model(models.Model):
    video_title = models.CharField(max_length=255)
    video_content = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    favorites = models.ManyToManyField(user, related_name='favorite_videos', blank=True)

    def __str__(self):
        return self.video_title

class User(AbstractBaseUser):
    user_name = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['phone_number', 'email']

    def __str__(self):
        return self.user_name

class Comment(models.Model):
    comment_text = models.TextField()
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video_model, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
# Create your models here.
