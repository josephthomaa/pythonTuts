from rest_framework import viewsets,permissions,status
from rest_framework.views import APIView, Response
from .models import ExpenseCategory, Expense
from .serializers import ExpenseSerializer, ExpenseCategorySerializer ,ExpenseDetailSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.filter(expense_user=8)
    #queryset = Expense.objects.all()
    #queryset = Expense.objects.raw('select *,b.name from rental_expense a join rental_expensetype b on a.ExpenseType_id = b.id ;')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ExpenseSerializer

class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer

class ExpenseDetailViewSet(viewsets.ModelViewSet):
    #queryset = ExpenseCategory.objects.filter(expense__ExpenseCategory__id=1)
    #queryset = ExpenseCategory.objects.filter(expense__expense_user__id__exact=1)
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseDetailSerializer


class CustomView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    def get(self, request, format=None):
        exp_usr = request.GET.get('q', '')
        if (exp_usr == ''):
            queryset = Expense.objects.all()

        else:
            queryset = Expense.objects.filter(expense_user=exp_usr)
        serializer_class = ExpenseSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Invalid Request")

    def put(self, request, format=None):
        expense = Expense.objects.get(pk=request.data['id'])
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        expense_id = Expense.objects.get(pk=request.data['id'])
        expense_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


