from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField("Title", max_length=255)
    description = models.TextField("Description")
    posted_date = models.DateTimeField("Posted date", default=datetime.now)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return self.title


