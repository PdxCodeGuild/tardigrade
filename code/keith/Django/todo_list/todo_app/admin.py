from django.contrib import admin

# Register your models here.
from.models import Todo
admin.site.register(Todo)   ### this registers my model to my admin page 