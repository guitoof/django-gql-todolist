from graphene import relay
from graphene_django import DjangoConnectionField, DjangoObjectType

from .models import Todo, TodoList


class TodoListNode(DjangoObjectType):
    class Meta:
        model = TodoList
        interfaces = (relay.Node, )


class TodoNode(DjangoObjectType):
    class Meta:
        model = Todo
        interfaces = (relay.Node, )


class Query(object):
    todos = DjangoConnectionField(TodoNode)
    todo = relay.Node.Field(TodoNode)
    todo_lists = DjangoConnectionField(TodoListNode)
    todo_list = relay.Node.Field(TodoListNode)
