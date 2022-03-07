from multiprocessing import context
from django.shortcuts import render, HttpResponse

# find whatsapp


def index(request):
    context = {
        'variable': "55LPA"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is home page")
# Create your views here.


def apps(request):
    return render(request, apps.html)
