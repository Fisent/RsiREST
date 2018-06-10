class Product():
    def __init__(self, name, description, price, datetime_created):
        self.name = name
        self.description = description
        self.price = price
        self.datetime_created = datetime_created

    def __str__(self):
        return '%s (%s PLN)' % (self.name, self.price)