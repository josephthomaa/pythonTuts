from rest_framework import viewsets,permissions
from .models import ExpenseCategory, Expense 
from .serializers import ExpenseSerializer, ExpenseCategorySerializer ,ExpenseDetailSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().select_related()
    #queryset = Expense.objects.raw('select *,b.name from rental_expense a join rental_expensetype b on a.ExpenseType_id = b.id ;')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ExpenseSerializer
 
class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer

class ExpenseDetailViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseDetailSerializer    

