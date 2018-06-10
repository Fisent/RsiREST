import json

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
        print(response.body)
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
        response = api.product.destroy(input('Id: '), body=None, params={}, headers={})
        print('Status code: ' + str(response.status_code))
    except Exception as ex:
        print(ex)


def list(api):
    try:
        response = api.product.list(body=None, params={}, headers={})
        for product in response.body['objects']:
            print(product)
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

        if input_text == 'c':
            create(api)
        elif input_text == 'r':
            read(api)
        elif input_text == 'u':
            update(api)
        elif input_text == 'd':
            delete(api)
        elif input_text == 'l':
            list(api)
        elif input_text == 'h':
            help()
        elif input_text == 'exit' or input_text == 'e':
            return
        else:
            print('Wrong command')