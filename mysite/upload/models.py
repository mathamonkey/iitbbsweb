from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class File(models.Model):
    uploaded_file_url = models.TextField(default='0000000')
    School = models.CharField(max_length=100, default='0000000')
    SubName = models.CharField(max_length=100, default='0000000')
    SubCode = models.CharField(max_length=100, default='0000000')
    Paper = models.CharField(max_length=100, default='0000000')
    Year = models.CharField(max_length=100, default='0000000')
    Author = models.CharField(max_length=30, default='Anonymus', )
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.SubName

