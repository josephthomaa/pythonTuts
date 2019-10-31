from django.shortcuts import render
 
from rest_framework import viewsets,status
from rest_framework.views import APIView, Response
from .models import ExpenseType, Expense ,Album , Track
from .serializers import ExpenseTypeSerializer, ExpenseSerializer, CustomExpenseSerializer , AlbumSerializer, TrackSerializer
from django.db.models import Count, Sum
import json
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated 
 
class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().select_related()
    #queryset = Expense.objects.raw('select *,b.name from rental_expense a join rental_expensetype b on a.ExpenseType_id = b.id ;')
    serializer_class = ExpenseSerializer
 
class ExpenseTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ExpenseType.objects.all()
    serializer_class = ExpenseTypeSerializer

class CustomView(APIView):
    def get(self, request, format=None):
        exp_type = request.GET.get('q', '')
        if(exp_type == ''):
            #queryset = Expense.objects.all()
            queryset = Expense.objects.values('expense_name').annotate(expense_amt=Sum('expense_amt')).order_by()
            #queryset = Expense.objects.raw('select id,expense_name,sum(expense_amt) as expense_amt ,expense_date from myapp_expense group by expense_name;')
            
        else:
            queryset = Expense.objects.filter(expense_name=exp_type)
        serializer_class = CustomExpenseSerializer(queryset, many=True)
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

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer        
