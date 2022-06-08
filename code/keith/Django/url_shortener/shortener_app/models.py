from django.db import models

# Create your models here.

class shortenURL(models.Model):
    original_url = models.URLField(max_length=10000)
    shortened_url = models.CharField(max_length = 5)

    def __str__(self):
        return self.original_url     