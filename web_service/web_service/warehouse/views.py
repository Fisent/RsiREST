from django.shortcuts import render, HttpResponse
from simple_rest_client.api import API
from json import load

# Create your views here.


class Product():
    def __init__(self, dict):
        self.name = dict['name']
        self.description = dict['description']
        self.price = dict['price']
        self.datetime_created = dict['datetime_created']

    def __str__(self):
        return '%s, %s (%s PLN)' % (self.name, self.description, self.price)


def list(request):
    api = API(
        api_root_url='http://127.0.0.1:8005/api/',
        params={},
        headers={},
        timeout=2,
        append_slash=True,
        json_encode_body=True
    )

    api.add_resource(resource_name='product')

    result = ''

    try:
        response = api.product.list(body=None, params={}, headers={})
        for product in response.body['objects']:
            product = Product(product)
            print(product)
            result += str(product) + '<br>'
    except Exception as ex:
        print(ex)

    return HttpResponse('Produkty:<br>' + result)