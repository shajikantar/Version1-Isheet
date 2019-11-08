from django.db import models

class contact():
    id = models.CharField(max_length=5)
    ImgName = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    passion = models.CharField(max_length=100)
    mailid = models.CharField(max_length=100)

class projectdetails(models.Model):
    Email = models.CharField(max_length=70)
    ProjectName = models.CharField(max_length=70)
    UserName = models.CharField(max_length=70)
    Company = models.CharField(max_length=70)
    Contact = models.CharField(max_length=70)
    InitialPassword = models.CharField(max_length=70)

class Is_details(models.Model):
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
