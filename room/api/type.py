from room.models import Category, Room, Entry
from strawberry_django_plus import gql
from strawberry import auto
from typing import Optional

@gql.django.type(Category)
class CategoryType:
    id : auto
    name : auto

@gql.django.type(Room)
class RoomType:
    id : auto
    name : auto
    created_at : auto

@gql.django.type(Entry)
class EntryType:
    id : auto
    created_at : auto
    is_valid : auto
    title : auto
    content: auto
    category : CategoryType
    room : RoomType
    votes : auto
    parent : Optional["EntryType"]
