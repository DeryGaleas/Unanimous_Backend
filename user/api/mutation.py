from user.models import User
from user.api.type import UserType
from user.api.input import UserCreateInput, UserDeleteInput
from strawberry_django_plus import gql
from strawberry.types import Info
from asgiref.sync import sync_to_async
from .utils import login_required_decorator


@gql.type()
class Mutation:
    login : UserType = gql.django.auth.login()
    logout = gql.django.auth.logout()

    @gql.django.field
    async def create_user(self, info:Info, data:UserCreateInput) -> UserType:
        user = await sync_to_async(User.objects.create_user)(**data.__dict__)
        return user

    @gql.django.field
    @login_required_decorator
    async def delete_user(self, info:Info, data:UserDeleteInput) -> bool:
        user: User = info.variable_values.get("user")
        print(user)
        if user.check_password(data.password):
            await sync_to_async(user.delete)()
            return True
        return False 
    


        