import graphene
from graphene import relay as relay
from typing import Any

class SomeTypeOne(graphene.ObjectType): ...
class SomeTypeTwo(graphene.ObjectType): ...

class MyUnion(graphene.Union):
    class Meta:
        types: Any = ...

def test_issue() -> None: ...
