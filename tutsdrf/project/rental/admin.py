from django.contrib import admin
from .models import ExpenseType, Expense ,Album ,Track

admin.site.register(ExpenseType)
admin.site.register(Expense)
admin.site.register(Album)
admin.site.register(Track)

# Register your models here.
