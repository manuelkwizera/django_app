from django.db import models

# Create your models here.
class Student(models.Model):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    date_of_birth   = models.DateField()
    email           = models.EmailField(unique=True)
    enrollment_date = models.DateField()
