import uuid
from room.models import Category, Room, Entry
from strawberry_django_plus import gql
from user.api.utils import login_required_decorator
from room.api.input import CategoryCreateInput, RoomCreateInput, EntryCreateInput, EntryUpdateVotesInput, MergeEntriesInput
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

   @gql.django.field
   async def create_entry(self, info:Info, data:EntryCreateInput) -> EntryType:
      entry : Entry = await Entry.objects.acreate(**data.__dict__)
      return entry

   @gql.django.field
   async def update_entry_votes(self, info:Info, data:EntryUpdateVotesInput) -> EntryType:
      entry : Entry = await Entry.objects.aget(id = data.id)
      entry.votes = data.votes
      sync_to_async(entry.save)()
      return entry

   @gql.django.field
   async def merge_entries(self, info:Info, data:MergeEntriesInput) -> EntryType:
      entry1 : Entry = await Entry.objects.aget(id = data.entry1_id)
      entry2 : Entry = await Entry.objects.aget(id = data.entry2_id)
      room_id = entry1.room_id
      parent_entry = await Entry.objects.acreate(title=data.title, content=data.content, category_id=data.category_id, room_id=room_id)
      entry1.parent = parent_entry
      entry2.parent = parent_entry
      await sync_to_async(entry1.save)()
      await sync_to_async(entry2.save)()
      return parent_entry 
