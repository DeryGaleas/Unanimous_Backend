from user.models import User
from strawberry_django_plus import gql
from strawberry import auto


@gql.django.input(User)
class UserCreateInput:
    username : auto
    password : auto
    email : auto
    first_name : auto
    last_name : auto

@gql.django.input(User)
class UserDeleteInput:
    password : auto
