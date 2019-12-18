from ..base import BaseOptions as BaseOptions, BaseType as BaseType
from typing import Any

class CustomOptions(BaseOptions): ...

class CustomType(BaseType):
    @classmethod
    def __init_subclass_with_meta__(cls, **options: Any) -> None: ...

def test_basetype() -> None: ...
def test_basetype_nones() -> None: ...
def test_basetype_custom() -> None: ...
def test_basetype_create() -> None: ...
def test_basetype_create_extra() -> None: ...