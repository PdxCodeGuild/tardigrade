from contextlib import nullcontext
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=500)
    complete = models.BooleanField(default = False)
    created_date = models.DateField(auto_now_add=True)
    completed_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.title