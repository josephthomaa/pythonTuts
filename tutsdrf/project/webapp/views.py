from django.shortcuts import render
from django.http import HttpResponse
from project.rental.models import ExpenseType

# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='webapp/home.html',
                  context = {"expenses":ExpenseType.objects.all})