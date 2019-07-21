

from django.db import models

# Create your models here.
class Employee(models.Model):
    Employee_id = models.IntegerField(max_length = 20,unique= True)
    Employee_name = models.CharField(max_length =20,default=0)
    Employee_email = models.EmailField(max_length = 30)
    Employee_salary = models.IntegerField(max_length = 40,default=0)


    def __str__(self):
        return "__all__"

