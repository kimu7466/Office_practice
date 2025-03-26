from rest_framework import serializers
from .models import Departments, Employee

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id','d_name','about']

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'profile', 'dept', 'name', 'password']

 