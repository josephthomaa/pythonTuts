from django.shortcuts import render
 
from rest_framework import viewsets,status
from rest_framework.views import APIView, Response
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

class CustomView(APIView):
    def get(self, request, format=None):
        exp_type = request.GET.get('q', '')
        if(exp_type == ''):
            queryset = Expense.objects.all()
        else:
            queryset = Expense.objects.filter(expense_name=exp_type)
        serializer_class = ExpenseSerializer(queryset, many=True)
        return Response(serializer_class.data)
 
    def post(self, request, format=None):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Some Post Response")  

    def put(self, request, format=None):
        expense = Expense.objects.get(pk=request.data['id'])
        serializer = ExpenseSerializer(expense,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        expense_id = Expense.objects.get(pk=request.data['id'])
        expense_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
            
