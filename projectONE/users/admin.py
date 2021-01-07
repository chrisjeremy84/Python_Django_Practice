from django.contrib import admin
from .models import Profile

# Register your models here.
#Here you can register models so they can show up in the admin page
#Start by importing the model created and adding it to the admin site by;
#passing it in the admin.site.register(<model>)
#This will make thhe model you've created accessable from the admin site.
admin.site.register(Profile)