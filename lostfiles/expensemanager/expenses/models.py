from django.db import models
from django.utils.timezone import now

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
    expense_name = models.CharField(max_length=50)
    expense_amt = models.IntegerField()
    expense_date = models.DateTimeField(default=now, editable=True)

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    def __unicode__(self):
        return '%s %s' % (self.expense_name, self.expense_amt)    

