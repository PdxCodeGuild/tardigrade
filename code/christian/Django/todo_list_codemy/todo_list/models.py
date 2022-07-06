from django.db import models

# Create your models here.

class List(models.Model):
    item = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    date_completed = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed) + ' | ' + str(self.date_created)+ ' | ' + str(self.date_completed)
    
        