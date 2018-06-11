import json
from product import Product


def create(api):

    body = {'name': input('Product name: '),
            'description': input('Product description: '),
            'price': input('Product price: ')}
    headers = {'Content-Type': 'application/json'}
    try:
        response = api.product.create(body=body, params={}, headers=headers)
        print('Status code: ' + str(response.status_code))
    except Exception as ex:
        print(ex)


def read(api):
    id = input('Id: ')
    try:
        response = api.product.retrieve(int(id), body=None, params=None, headers=None)
        print('Status code: ' + str(response.status_code))
        product = Product(response.body)
        print(product)
    except:
        print('No such object')


def update(api):
    id = int(input('Id: '))
    body = {'name': input('Product name: '),
            'description': input('Product description: '),
            'price': input('Product price: ')}
    headers = {'Content-Type': 'application/json'}
    try:
        response = api.product.update(id, body=body, params={}, headers=headers)
        print('Status code: ' + str(response.status_code))
    except Exception as ex:
        print(ex)

def delete(api):
    try:
        input_text = input('Id: ')
        for id in input_text.split():
            response = api.product.destroy(id, body=None, params={}, headers={})
            print('Status code: ' + str(response.status_code))
    except Exception as ex:
        print(ex)


def list(api):
    try:
        response = api.product.list(body=None, params={}, headers={})
        for product in response.body['objects']:
            pr = Product(product)
            print(pr)
    except Exception as ex:
        print(ex)


def help():
    print('Select action:')
    print('Create product (c)')
    print('Read product information (r)')
    print('Update product data (u)')
    print('Delete product (d)')
    print('List all objects (l)')
    print('Help (h)')
    print("Exit (e)")

def cli(api):
    running = True
    help()
    while(running):
        input_text = input(">")

        if input_text == 'c' or input_text == 'create':
            create(api)
        elif input_text == 'r' or input_text == 'read':
            read(api)
        elif input_text == 'u' or input_text == 'update':
            update(api)
        elif input_text == 'd' or input_text == 'delete':
            delete(api)
        elif input_text == 'l' or input_text == 'list' or input_text == 'ls':
            list(api)
        elif input_text == 'h' or input_text == 'help':
            help()
        elif input_text == 'exit' or input_text == 'e':
            return
        else:
            print('Wrong command')