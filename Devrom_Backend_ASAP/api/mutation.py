from strawberry_django_plus import gql
from room.api.mutation import Mutation as RoomMutation
from user.api.mutation import Mutation as UserMutation

@gql.type
class Mutation(RoomMutation, UserMutation):
    pass

