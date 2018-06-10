from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from .models import Product
from tastypie.authorization import Authorization

class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        authorization = Authorization()
        serializer = Serializer(formats=['json'],)
