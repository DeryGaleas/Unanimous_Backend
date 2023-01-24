import uuid
from room.models import Category, Room, Entry
from strawberry_django_plus import gql
from user.api.utils import login_required_decorator, get_lazy_query_set_as_list
from room.api.input import CategoryCreateInput, RoomCreateInput, EntryCreateInput, EntryUpdateVotesInput, MergeEntriesInput, DismergeEntriesInput, UpdateEntriesCategoryInput, DeleteEntryInput
from room.api.type import CategoryType, RoomType, EntryType
from asgiref.sync import sync_to_async 
from strawberry.types import Info
from typing import List

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
      entries: List[Entry] = await get_lazy_query_set_as_list(Entry.objects.filter(id__in=data.entries_id))
      room_id = entries[0].room_id
      votes = 0
      parent_entry = await Entry.objects.acreate(title=data.title, content=data.content, category_id=data.category_id, room_id=room_id)
      for entry in entries:
         votes += entry.votes
         entry.parent = parent_entry
         entry.is_children = True       
         await sync_to_async(entry.save)()
      parent_entry.votes = votes
      await sync_to_async(parent_entry.save)()
      return parent_entry 

   @gql.django.field
   async def dismerge_entries(self, info:Info, data:DismergeEntriesInput) -> List[EntryType]:
      #parent_entry = await Entry.objects.aget(id=data.parent_id)
      children : List[Entry] = await get_lazy_query_set_as_list(Entry.objects.filter(id__in=data.children_id))
      for child in children:
         child.parent = None
         child.is_children = False
         await sync_to_async(child.save)()
      return children

   @gql.django.field
   async def update_entries_category(self, info:Info, data:UpdateEntriesCategoryInput) -> List[EntryType]:
      entries : List[Entry] = await get_lazy_query_set_as_list(Entry.objects.filter(id__in=data.entries_id))
      for entry in entries:
         entry.category_id = data.Category_id
         await sync_to_async(entry.save)()

      return entries 

   @gql.django.field
   async def delete_entry(self, info:Info, data: DeleteEntryInput) -> bool:
      try:
         entry : Entry = await Entry.objects.aget(id=data.entry_id)
         await sync_to_async(entry.delete)()
         return True
      except:
         raise Exception("Error deleting the object")
      


   

   

   




#dismerge entry individualmente y multiples
#update category - list de la entries para actualizar en bulk _Funciones de django
#eliminar entries
# 

