from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    price = models.FloatField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s (%s PLN)' % (self.name, self.price)