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




