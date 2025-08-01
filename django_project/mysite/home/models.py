from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=90, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)