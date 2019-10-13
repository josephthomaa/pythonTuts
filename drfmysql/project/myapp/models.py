from django.db import models
 
class University(models.Model):
    name = models.CharField(max_length=50)
 
    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"
 
    def __unicode__(self):
        return self.name
 
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.DO_NOTHING)
 
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
 
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Expense(models.Model):
    expense_name = models.CharField(max_length=50)
    expense_amt = models.IntegerField()        

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    def __unicode__(self):
        return '%s %s' % (self.expense_name, self.expense_amt)    

        