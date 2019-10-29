from rest_framework import serializers
from .models import ExpenseType, Expense, Album ,Track


class ExpenseSerializer(serializers.ModelSerializer):
    #expenseType = ExpenseTypeSerializer(read_only=True)
    
    class Meta:
        model = Expense
        fields = '__all__'

class ExpenseTypeSerializer(serializers.ModelSerializer):
    expense = ExpenseSerializer(many=True)
    class Meta:
        model = ExpenseType
        fields = ('id', 'name', 'expense')        

class CustomExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense        
        fields = ('expense_name','expense_amt')  

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']       

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')              