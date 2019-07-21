from rest_framework import serializers
from django.db import models
from accounts.models import Employee
from rest_framework import exceptions
from django.contrib.auth import authenticate,login

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields  = ('Employee_id','Employee_name','Employee_email','Employee_salary')



