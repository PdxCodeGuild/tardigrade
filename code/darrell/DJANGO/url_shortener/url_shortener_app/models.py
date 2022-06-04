from django.db import models


class UrlShortener(models.Model):
    code = models.CharField(max_length=6)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.code
