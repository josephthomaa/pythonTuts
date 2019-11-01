from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class ExpenseCategory(models.Model):
    cat_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=now, editable=True)

    class Meta:
        verbose_name = "ExpenseCategory"
        verbose_name_plural = "ExpenseCategorys"

    def __unicode__(self):
        return self.cat_name    

class Expense(models.Model):
    ExpenseCategory = models.ForeignKey(ExpenseCategory,related_name='expense', on_delete=models.DO_NOTHING) 
    expense_user = models.ForeignKey(User, related_name='user', on_delete=models.DO_NOTHING , null=True)   
    expense_name = models.CharField(max_length=50)
    expense_amt = models.IntegerField()
    expense_date = models.DateTimeField(default=now, editable=True)

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    def __unicode__(self):
        return '%s %s' % (self.expense_name, self.expense_amt)    

