from room.api.query import Query as RoomQuery
from strawberry_django_plus import gql



@gql.type
class Query(RoomQuery):
    pass

