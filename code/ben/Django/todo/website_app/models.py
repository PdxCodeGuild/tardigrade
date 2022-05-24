from django.db import models
from django.contrib.auth.models import User

class todo(models.Model):
        title = models.CharField(max_length = 200)
        text = models.TextField(max_length = 500)
        create_date = models.DateField()
        complete = models.BooleanField(default = False)

        def __str__(self):
            return self.title