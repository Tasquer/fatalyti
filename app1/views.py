from django.shortcuts import render
from django.http import HttpResponse

def index_app1(request):
    return HttpResponse("<h1>Hola, esta es la App 1</h1>")
