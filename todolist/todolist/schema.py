from graphene import Schema, ObjectType

import todos.schema


class Query(todos.schema.Query, ObjectType):
    pass


schema = Schema(query=Query)
