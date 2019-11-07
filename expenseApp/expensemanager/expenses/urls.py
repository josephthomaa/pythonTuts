from rest_framework import routers
from django.conf.urls import url
from .api import ExpenseCategoryViewSet, ExpenseViewSet ,ExpenseDetailViewSet, CustomView

router = routers.DefaultRouter()
router.register(r'expenses', ExpenseViewSet)
router.register(r'expensecategory', ExpenseCategoryViewSet)
router.register(r'expensedetail', ExpenseDetailViewSet)

urlpatterns = [
    url(r'customview', CustomView.as_view()),

]

urlpatterns += router.urls