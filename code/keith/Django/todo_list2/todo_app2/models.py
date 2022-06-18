from django.db import models

# Create your models here.



class Todo(models.Model):      ### this is the model or basically spreadsheet or data table for my todo list
        title = models.CharField(max_length = 200)
        start_date = models.DateField()
        end_date = models.DateField()
        completed = models.BooleanField()

        def __str__(self):
            return self.title
