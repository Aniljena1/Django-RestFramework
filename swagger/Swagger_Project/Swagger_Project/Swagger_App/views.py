
from django.shortcuts import render
from Swagger_App.models import Employee
from Swagger_App.serializers import EmployeeSerializer
from rest_framework import generics

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class Employee_List_Swagger_View(generics.ListCreateAPIView):
    """
       list:
          Return a list of all Employees.
       create:
           Create a new Employee.
       """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)



class Employee_Detail_Swagger_View(generics.RetrieveUpdateDestroyAPIView):
    """
            retrieve:
                Return the given Employee.
            destroy:
                Delete a given Employee.
            update:
               Update a given Employee.
            partial_update:
                 Partial Up date a given Employee.
        """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer




