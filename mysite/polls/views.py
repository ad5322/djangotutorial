from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world! you are at polls index')

# Create your views here.
