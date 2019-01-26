from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse



def index (request):
    return HttpResponse('<h1>Polls</h1>')

def json (request):
    return JsonResponse({'foo': 'bar'})