from graphene import Field
from graphene import String
from graphene import Mutation

from ingredients.models import Category
from ingredients.models import Ingredient
from api_graphql.objects import CategoryNode
from api_graphql.objects import IngredientNode
from api_graphql.inputs import CreateCategoryInput
from api_graphql.inputs import CreateIngredientInput
from api_graphql.utils import transform_global_ids
from api_graphql.utils import delete_attributes_none

# Create your mutations here


class CreateCategory(Mutation):
    category = Field(CategoryNode)

    class Arguments:
        input = CreateCategoryInput(required=True)

    def mutate(self, info, input):
        category = Category.objects.create(**vars(input))

        return CreateCategory(category=category)


class CreateIngredient(Mutation):
    ingredient = Field(IngredientNode)

    class Arguments:
        input = CreateIngredientInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        ingredient = Ingredient.objects.create(**input)

        return CreateIngredient(ingredient=ingredient)
