import functools
from typing import List
from asgiref.sync import sync_to_async
from django.db.models import QuerySet
from ..models import User as UserModel

@sync_to_async
def get_current_user_from_info(info):
    user = info.context.request.user
    if isinstance(user, UserModel):
        pass
    return user


async def get_lazy_query_set_as_list(query_set: QuerySet) -> List:
    list_coroutine = sync_to_async(list)
    return await list_coroutine(query_set)


def login_required_decorator(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        info = kwargs.get("info")
        user = await get_current_user_from_info(info)

        if not user.is_authenticated:
            raise Exception("User is not logged in")
        info.variable_values["user"] = user    
        return await func(*args, **kwargs)
    
    return wrapper
