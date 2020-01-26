from graphene import Field
from graphene import String
from graphene import Mutation

from ingredients.models import Category
from ingredients.models import Ingredient
from api_graphql.objects import CategoryNode
from api_graphql.objects import IngredientNode
from api_graphql.inputs import UpdateCategoryInput
from api_graphql.inputs import UpdateIngredientInput
from api_graphql.utils import transform_global_ids
from api_graphql.utils import delete_attributes_none

# Create your mutations here


class UpdateCategory(Mutation):
    category = Field(CategoryNode)

    class Arguments:
        input = UpdateCategoryInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Category.objects.filter(pk=input.get('id')).update(**input)
        category = Category.objects.get(pk=input.get('id'))

        return UpdateCategory(category=category)


class UpdateIngredient(Mutation):
    ingredient = Field(IngredientNode)

    class Arguments:
        input = UpdateIngredientInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Ingredient.objects.filter(pk=input.get('id')).update(**input)
        ingredient = Ingredient.objects.get(pk=input.get('id'))

        return UpdateIngredient(ingredient=ingredient)
