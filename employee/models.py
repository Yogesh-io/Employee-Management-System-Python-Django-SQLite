from django.db import models
from django.core.validators import *
from .validators import *

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=50, validators=[validate_name])
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    salary = models.DecimalField( max_digits=10, decimal_places=2 , validators=[validate_salary])
    doj = models.DateField()
    mobile = models.CharField(max_length=10,validators=[RegexValidator(r'^[6-9]\d{9}$')])
    profile_pic= models.ImageField(upload_to='employees_pic/',null=True,blank=True)
    resumes = models.FileField(upload_to='employees_resumes/',blank=True)

    def __str__(self):
        return self.name