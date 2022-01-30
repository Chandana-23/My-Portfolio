from django.db import models

# Create your models here.
class Skills(models.Model):
    skills = models.CharField(max_length=150)

class Projects(models.Model):
    topic = models.CharField(max_length=150)
    project_name = models.CharField(max_length=250)
    project_desc = models.TextField()

class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    pic = models.ImageField(upload_to='media/')
    desc = models.TextField()
    info = models.TextField()

class Query(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=250)
    message = models.TextField()