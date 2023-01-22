from .type import UserType
from strawberry_django_plus import gql
from strawberry.types import Info
from .utils import login_required_decorator

@gql.type
class Query:

    @gql.django.field
    @login_required_decorator
    async def me(self, info:Info) -> UserType:
        user = info.variable_values.get("user")
        return user