from graphene import ID
from graphene import String
from graphene import InputObjectType


# Create your inputs types here.


class CreateCategoryInput(InputObjectType):
    name = String(required=True)


class UpdateCategoryInput(InputObjectType):
    id = ID(required=True)
    name = String()


class CreateIngredientInput(InputObjectType):
    name = String(required=True)
    notes = String(required=True)
    category_id = ID(required=True)


class UpdateIngredientInput(InputObjectType):
    id = ID(required=True)
    name = String()
    notes = String()
    category_id = ID()
