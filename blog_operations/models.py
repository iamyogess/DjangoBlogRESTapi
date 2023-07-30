from django.db import models
from accounts.models import User

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    blog_image = models.ImageField(blank=True,default=None)
    blog_content = models.TextField()


    def __str__(self):
        return self.title
