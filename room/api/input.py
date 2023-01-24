from room.models import Category, Room, Entry
from strawberry_django_plus import gql
from strawberry import auto, ID 
import strawberry
from typing import List


@gql.django.input(Category)
class CategoryCreateInput:
    name : auto

@gql.django.input(Room)
class RoomCreateInput:
    name: auto


@gql.django.input(Entry)
class EntryCreateInput:
    title : auto
    content: auto
    category_id : ID
    room_id : strawberry.scalars.ID
    votes : auto

@gql.django.input(Entry)
class EntryUpdateVotesInput:
    id : ID
    votes : auto

@gql.django.input(Entry)
class MergeEntriesInput:
    entries_id : List[ID]
    title : auto
    content : auto
    category_id : ID

@gql.django.input(Entry)
class DismergeEntriesInput:
    parent_id : ID
    children_id : List[ID]

@gql.django.input(Entry)
class UpdateEntriesCategoryInput:
    entries_id : List[ID]
    Category_id : ID


@gql.django.input(Entry)
class DeleteEntryInput:
    entry_id : ID






