from graphene import relay
from graphene_django import DjangoConnectionField, DjangoObjectType

from .models import Todo


class TodoNode(DjangoObjectType):
    class Meta:
        model = Todo
        interfaces = (relay.Node, )


class Query(object):
    todos = DjangoConnectionField(TodoNode)
