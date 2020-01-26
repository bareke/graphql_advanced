from graphene.relay import Node
from graphene_django import DjangoObjectType

from ingredients.models import Category
from ingredients.models import Ingredient
from .connections import TotalCountConnection

# Create your objects types here.


class CategoryNode(DjangoObjectType):

    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class IngredientNode(DjangoObjectType):

    class Meta:
        model = Ingredient
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
