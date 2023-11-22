from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Main page')


def abaut(request):
    return HttpResponse('Abaut my site')

def contacts(request):
    return HttpResponse('My contacts')