from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_univer_info(request):
    return HttpResponse('Enter your university name: ')
