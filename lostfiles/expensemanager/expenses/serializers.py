from rest_framework import serializers
from .models import ExpenseCategory, Expense 

class ExpenseSerializer(serializers.ModelSerializer):
    #expenseType = ExpenseTypeSerializer(read_only=True)
    
    class Meta:
        model = Expense
        fields = '__all__'

class ExpenseDetailSerializer(serializers.ModelSerializer):
    expense = ExpenseSerializer(many=True)
    class Meta:
        model = ExpenseCategory
        fields = ('id', 'cat_name', 'expense')   

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'  
