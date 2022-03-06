from multiprocessing import context
from django.shortcuts import render, HttpResponse


def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is home page")
# Create your views here.
