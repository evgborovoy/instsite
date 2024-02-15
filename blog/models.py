from django.db import models
from django.utils import timezone

class Post(models.Model):


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "post"
        ordering = ("-published",)

    def __str__(self):
        return self.title
