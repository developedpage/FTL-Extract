from __future__ import annotations

from typing import TYPE_CHECKING

from fluent.syntax import FluentSerializer, ast

if TYPE_CHECKING:
    from ftl_extract.matcher import FluentKey


def comment_ftl_key(key: FluentKey, serializer: FluentSerializer) -> None:
    pass
