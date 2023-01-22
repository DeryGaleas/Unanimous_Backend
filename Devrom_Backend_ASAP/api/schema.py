from strawberry import Schema
from Devrom_Backend_ASAP.api.mutation import Mutation

from Devrom_Backend_ASAP.api.query import Query

schema = Schema(query=Query, mutation=Mutation)
