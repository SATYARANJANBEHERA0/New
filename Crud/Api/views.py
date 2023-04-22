from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user.employee)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(employee=self.request.user.employee)

    def perform_destroy(self, instance):
        instance.status = 'DELETED'
        instance.save()
