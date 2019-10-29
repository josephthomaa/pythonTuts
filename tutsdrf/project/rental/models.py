from django.db import models
from django.utils.timezone import now
from django.http import JsonResponse

# Create your models here.
class ExpenseType(models.Model):
    name = models.CharField(max_length=50)
 
    class Meta:
        verbose_name = "ExpenseType"
        verbose_name_plural = "ExpenseTypes"
 
    def __unicode__(self):
        return self.name
 
class Expense(models.Model):
    expense_name = models.CharField(max_length=50)
    expense_amt = models.IntegerField()
    expense_date = models.DateTimeField(default=now, editable=True)
    ExpenseType = models.ForeignKey(ExpenseType,related_name='expense', on_delete=models.DO_NOTHING)        

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    def __unicode__(self):
        return '%s %s' % (self.expense_name, self.expense_amt)   

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        #return {"order": "{}", "title": "{}", "duration": "{}".format(self.order, self.title,self.duration)}
        return '%d: %s  %s' % (self.order, self.title, self.duration)         

