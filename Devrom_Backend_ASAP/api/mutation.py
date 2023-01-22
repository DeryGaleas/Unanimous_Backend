from strawberry_django_plus import gql
from room.api.mutation import Mutation as RoomMutation

@gql.type
class Mutation(RoomMutation):
    pass

