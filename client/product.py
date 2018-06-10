class Product():
    def __init__(self, dict):
        self.id = dict['id']
        self.name = dict['name']
        self.description = dict['description']
        self.price = dict['price']
        self.datetime_created = dict['datetime_created']

    def __str__(self):
        return '#%s| %s, %s (%s PLN)' % (self.id, self.name, self.description, self.price)