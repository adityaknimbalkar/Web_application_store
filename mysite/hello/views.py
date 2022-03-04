from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("this is home page")
# Create your views here.
