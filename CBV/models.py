from django.db import models

# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=256)
    principal=models.CharField(max_length=256)
    address=models.CharField(max_length=256)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name=models.CharField(max_length=256)
    school=models.ForeignKey(School,related_name='student')
    age=models.PositiveIntegerField()

    def __str__(self):
        return self.name
    