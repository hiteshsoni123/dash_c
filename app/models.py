from tabnanny import check
from django.db import models
from datetime import date

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=30,unique=True)
    date_of_birth = models.DateField()
    employee_contact = models.CharField(max_length=15)
    employee_email = models.EmailField()
    employee_designation = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    employee_image = models.ImageField()
    password = models.CharField(max_length=30, default=True)
    
class Emp_login(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)

class Holiday(models.Model):
    day = models.CharField(max_length=30)
    date = models.DateField()
    occassion = models.CharField(max_length=50)
    holiday_over = models.CharField(max_length=20, null=True)

    def eligiblity(self):
        current_date = date.today()
        if current_date > self.date:
            return True
        else:
            return False
    