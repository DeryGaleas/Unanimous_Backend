import uuid
from room.models import Category, Room, Entry
from strawberry_django_plus import gql
from user.api.utils import login_required_decorator
from room.api.input import CategoryCreateInput, RoomCreateInput
from room.api.type import CategoryType, RoomType, EntryType
from asgiref.sync import sync_to_async 
from strawberry.types import Info
from user.models import User

@gql.type
class Mutation:

   @gql.django.field
   async def create_category(self, info:Info, data:CategoryCreateInput) -> CategoryType:
      category_name_exists = await Category.objects.filter(name=data.name).aexists()
      if category_name_exists:
         raise Exception("The category name is not unique")
      category : Category = await Category.objects.acreate(name=data.name)
      return category

   @gql.django.field
   async def create_room(self, info:Info, data:RoomCreateInput)-> RoomType:
      room : Room = await Room.objects.acreate(name=data.name)
      return room

    
