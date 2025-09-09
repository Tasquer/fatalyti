from django.shortcuts import render
from django.http import HttpResponse

def index_app2(request):
    return HttpResponse("<h1>Hola, esta es la App 2</h1>")
