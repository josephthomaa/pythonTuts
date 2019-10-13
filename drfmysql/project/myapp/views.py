from django.shortcuts import render
 
from rest_framework import viewsets
from .models import University, Student, Expense
from .serializers import UniversitySerializer, StudentSerializer, ExpenseSerializer
 
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
 
class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
