from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>MySecond App</h1>')
def help(request):
    dict1 = {'insertMe':"I am coming from views.py"}
    return render(request,'AppTwo/help.html',context=dict1)
