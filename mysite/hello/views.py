from ast import Name, Pass
import email
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, HttpResponse
from hello.models import Contact, Webstore
from django.contrib import messages


# find whatsapp


# def index(request):
# context = {
#  'variable': "55LPA"
# }
# return render(request, 'index.html')
# return HttpResponse("this is home page")
# Create your views here.


def apps(request):
    return render(request, 'apps.html')


def infos(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        con = Contact(Name=email, Email=name)
        con.save()
        messages.success(request, "data is saved")
    return render(request, 'info.html')


def tasks(request):
    alltask = Contact.objects.all()
    context = {"tasks": alltask}
    return render(request, 'apps.html', context)


def index(request):
    allapps = Webstore.objects.all()
    context = {"appslist": allapps}
    return render(request, 'index.html', context)


def app_byid(request):
    app_data = Webstore.objects.filter(App_name="Pubg2")
    context = {"appdata": app_data}
    return render(request, 'index.html', context)
