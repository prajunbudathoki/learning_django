from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    # return HttpResponse('hello world this is home page')
    return render(req,'index.html')

def about(req):
    return HttpResponse('hello world this is about page')
