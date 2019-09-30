from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def indexpage(request):
    return HttpResponse("welcome to my indexpage")
def contactpage(request):
    return HttpResponse("contactpage")
def homepage(request):
    return HttpResponse("welcome to home page")