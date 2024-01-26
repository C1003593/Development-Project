from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse('<h1>Test page</h1>')


