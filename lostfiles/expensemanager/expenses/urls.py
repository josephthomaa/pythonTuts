from rest_framework import routers
from .api import ExpenseCategoryViewSet, ExpenseViewSet ,ExpenseDetailViewSet

router = routers.DefaultRouter()
router.register(r'expenses', ExpenseViewSet)
router.register(r'expensecategory', ExpenseCategoryViewSet)
router.register(r'expensedetail', ExpenseDetailViewSet)


urlpatterns = router.urls