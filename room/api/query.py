from room.models import Category, Room, Entry
from strawberry_django_plus import gql
from strawberry.types import Info
from room.api.type import CategoryType, RoomType
from typing import List
 

@gql.type
class Query:

    @gql.django.field
    def get_all_categories(self, info:Info) -> List[CategoryType]:

        categories = Category.objects.all()
        return categories

    @gql.django.field
    def get_all_rooms(self, info:Info) -> List[RoomType]:
        rooms = Room.objects.all()
        return rooms