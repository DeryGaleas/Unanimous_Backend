from strawberry_django_plus import gql
from user.models import User
from strawberry import auto

@gql.django.type(User)
class UserType:
    id : auto
    username : auto
    email : auto
    first_name : auto
    last_name : auto
    last_login : auto
    is_active : auto

    