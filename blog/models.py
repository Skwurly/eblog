
from django.db import models
from ckeditor.fields import RichTextField
from datetime import date
# Create your models here.

class Post(models.Model):

    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    Date = models.DateField(default=date.today)
    Text = RichTextField()

    def __str__(self):
        return self.Title
