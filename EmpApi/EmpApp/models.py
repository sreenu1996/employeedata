import email
from django.db import models

# Create your models here.

class EmployeModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    phno=models.CharField(max_length=34)
    address=models.TextField()
    work_experience = models.JSONField()
    Qualification = models.JSONField()
    Project = models.JSONField()

    def __str__(self) -> str:
        return self.name