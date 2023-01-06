from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    salary=models.FloatField()
    email=models.CharField(max_length=300)
    class Meta:
        db_table = 'employee'