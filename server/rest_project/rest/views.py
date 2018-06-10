from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def new_method(request):
    if request.method != 'POST':
        return HttpResponse('Only POST request')

    how_many = json.loads(request.body)[['how_many']
    for i in range(how_many):
        print(i)

    return HttpResponse('Method ran')

