from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


# Create your views here.

def home(request):
    template = loader.get_template('Home.html')
    return HttpResponse(template.render({}, request))




