from django.shortcuts import render
from django.http import HttpResponse

def testapp(request):
    return HttpResponse("Hello <b>Django</b> Test Page")
