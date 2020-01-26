from graphene import ID
from graphene import Field
from graphene import Mutation
from graphql import GraphQLError
from graphql_relay.node.node import from_global_id

from ingredients.models import Category
from ingredients.models import Ingredient
from api_graphql.objects import CategoryNode
from api_graphql.objects import IngredientNode

# Create your mutations here


class DeleteCategory(Mutation):
    category = Field(CategoryNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            category = Category.objects.get(pk=input)
            Category.objects.filter(pk=input).delete()
        except Category.DoesNotExist:
            raise GraphQLError('Category does not delete')

        return DeleteCategory(category=category)


class DeleteIngredient(Mutation):
    ingredient = Field(IngredientNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            ingredient = Ingredient.objects.get(pk=input)
            Ingredient.objects.filter(pk=input).delete()
        except Ingredient.DoesNotExist:
            raise GraphQLError('Ingredient does not delete')

        return DeleteIngredient(ingredient=ingredient)
