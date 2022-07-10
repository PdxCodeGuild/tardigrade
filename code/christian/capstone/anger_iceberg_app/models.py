from django.db import models

# Create your models here.
class Quote(models.Model):
    text = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    helpful = models.BooleanField(default=False)

    def __str__(self):
        return ('QUOTE: ' + self.text + ' | AUTHOR: ' + self.author + ' | HELPFUL(?): ' + str(self.helpful))