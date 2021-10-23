from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context={}
    return render(request, 'index.html', context)
def register(request):
    context={}
    return render(request, 'registration_form.html', context)
