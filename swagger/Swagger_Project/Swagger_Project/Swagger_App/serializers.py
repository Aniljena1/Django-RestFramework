
from rest_framework import serializers
from Swagger_App.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta :
        model = Employee
        fields = '__all__'
