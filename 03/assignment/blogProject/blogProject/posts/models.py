from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
  pass

class Post(models.Model):
  title=models.CharField(max_length = 50)
  content = models.TextField()
  dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
  dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)
  author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  def __str__(self):
    return self.title


class Comment(models.Model):
  post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
  content = models.TextField()
  dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
  author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)