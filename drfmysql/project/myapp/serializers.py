from rest_framework import serializers
from .models import University, Student,Expense
 
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'
 
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense        
        fields = '__all__'

class CustomExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense        
        fields = ('expense_name','expense_amt')