from django.db import models

# Create your models here.

GENDER_CHOICES=(
    ('M','Male'),
    ('F','Female'),
    ('O','Others')
)

class Students(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.CharField(max_length=10)
    address=models.TextField()
    course=models.CharField(max_length=50)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
class Faculty(models.Model):
    Name=models.CharField(max_length=30)
    Destination=models.CharField(max_length=20)
    Department=models.CharField(max_length=30)
