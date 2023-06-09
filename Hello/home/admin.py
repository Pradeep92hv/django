from django.contrib import admin
from .models import ToDoList,Item
#  to add model to admin dashboard

# Register your models here.

admin.site.register(ToDoList),
admin.site.register(Item)