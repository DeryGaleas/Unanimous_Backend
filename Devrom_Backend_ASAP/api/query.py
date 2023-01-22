from strawberry_django_plus import gql
from room.api.query import Query as RoomQuery
from user.api.query import Query as UserQuery





@gql.type
class Query(RoomQuery, UserQuery):
    pass

