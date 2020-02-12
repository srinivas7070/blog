from django.db import models

class Job(models.Model):
   image = models.ImageField(upload_to='images/')
   summery = models.CharField(max_length=200)
   url1 = models.CharField(max_length=200)
   facultyname = models.CharField(max_length=50)