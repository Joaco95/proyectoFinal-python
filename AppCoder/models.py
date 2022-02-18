from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db.models.fields import (
    BooleanField, CharField, DateField, EmailField, IntegerField,
    GenericIPAddressField, URLField, DecimalField, TimeField
)
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Post(models.Model):
    title=models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    # body = models.TextField()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))