from django.shortcuts import render
from django.http import HttpResponse
import json
from random import randint, sample
import string

from .models import Product

# Create your views here.

def new_method(request):
    if request.method != 'POST':
        return HttpResponse('Only POST request')

    a = json.loads(request.body)['a']
    b = json.loads(request.body)['b']
    rand = randint(a, b)

    for i in range(rand):
        name = ''.join(sample(string.ascii_letters, 8))
        description = ''.join(sample(string.ascii_letters, 15))
        price = randint(0, 100)
        pr = Product(name=name, description=description, price=price)
        pr.save()

    return HttpResponse('Method ran')

