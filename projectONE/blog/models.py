from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# Here the classes created will be the tables of the database.
# And the attributes created in each class will be the fields of the table

class Post(models.Model):
    title  = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    