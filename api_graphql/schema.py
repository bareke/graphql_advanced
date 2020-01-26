from graphene_django.filter import DjangoFilterConnectionField
from graphene.relay import Node
from graphene import ObjectType

from .objects import CategoryNode
from .objects import IngredientNode

from ingredients.models import Category
from ingredients.models import Ingredient

from .mutations.create import CreateCategory
from .mutations.create import CreateIngredient
from .mutations.update import UpdateCategory
from .mutations.update import UpdateIngredient
from .mutations.delete import DeleteCategory
from .mutations.delete import DeleteIngredient
from .mutations.upload import UploadFile

# Schema definition


class Query(ObjectType):
    category = Node.Field(CategoryNode)
    ingredient = Node.Field(IngredientNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)


class Mutation(ObjectType):
    create_category = CreateCategory.Field()
    create_ingredient = CreateIngredient.Field()

    update_category = UpdateCategory.Field()
    update_ingredient = UpdateIngredient.Field()

    delete_category = DeleteCategory.Field()
    delete_ingredient = DeleteIngredient.Field()

    upload_file = UploadFile.Field()
