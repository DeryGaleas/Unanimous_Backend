from room.models import Category
from strawberry_django_plus import gql
from strawberry.types import Info
from room.api.type import CategoryType
from typing import List
 

@gql.type
class Query:

    @gql.django.field
    def categories(self, info:Info) -> List[CategoryType]:

        categories = Category.objects.all()
        return categories
