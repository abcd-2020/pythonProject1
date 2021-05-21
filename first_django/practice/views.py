from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def TellHello(requests):
    html = "<h1> 안녕!!! </h1>"
    return HttpResponse(html)