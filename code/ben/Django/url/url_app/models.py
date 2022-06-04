from django.db import models

class URL_Short(models.Model):
    url = models.CharField(max_length=200)
    url_short = models.CharField(max_length=20)
    
    def __str__(self):
        return self.url
