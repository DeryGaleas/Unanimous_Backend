from room.models import Category, Room, Entry
from strawberry_django_plus import gql
from strawberry import auto, ID 
import strawberry


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
    entry1_id : ID
    entry2_id : ID
    title : auto
    content : auto
    category_id : ID







