from pyexpat import model
from django.db import models
from datetime import datetime, date

# Create your models here.
# include: TodoItem model
# Contains: text description, create date, complete date, boolean for complete/uncomplete
# User should be presented with an input field and a button in a form
# When button is clicked, it shoudl save the data to the server and show onto the list

class TodoItem(models.Model):
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    complete_date =  models.DateField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.description