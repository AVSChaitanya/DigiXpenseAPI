#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr, MappedAsDataclass
from typing_extensions import Annotated

from app.utils.timezone import timezone_utils

# Universal Mapped type primary key, needs to be added manually, refer to the following usage methods
# MappedBase -> id: Mapped[id_key]
# DataClassBase && Base -> id: Mapped[id_key] = mapped_column(init=False)
id_key = Annotated[
    int, mapped_column(primary_key=True, index=True, autoincrement=True, sort_order=-999, comment='主键id')
]


# Mixin: an object-oriented programming concept that makes structures clearer, `Wiki <https://en.wikipedia.org/wiki/Mixin/>`__
class UserMixin(MappedAsDataclass):
    """User Mixin data class"""

    create_user: Mapped[int] = mapped_column(sort_order=998, comment='创建者')
    update_user: Mapped[int | None] = mapped_column(init=False, default=None, sort_order=998, comment='修改者')


class DateTimeMixin(MappedAsDataclass):
    """Date and time Mixin data class"""

    created_time: Mapped[datetime] = mapped_column(
        init=False, default_factory=timezone_utils.get_timezone_datetime, sort_order=999, comment='创建时间'
    )
    updated_time: Mapped[datetime | None] = mapped_column(
        init=False, onupdate=timezone_utils.get_timezone_datetime, sort_order=999, comment='更新时间'
    )


class MappedBase(DeclarativeBase):
    """
    Declarative base class, the original DeclarativeBase class, exists as the parent class of all base or data model classes

    `DeclarativeBase <https://docs.sqlalchemy.org/en/20/orm/declarative_config.html>`__
    `mapped_column() <https://docs.sqlalchemy.org/en/20/orm/mapping_api.html#sqlalchemy.orm.mapped_column>`__
    """

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class DataClassBase(MappedAsDataclass, MappedBase):
    """
    Declarative data class base class, which will come with data class integration, allowing more advanced configuration, but you must pay attention to some of its characteristics, especially when used with DeclarativeBase

    `MappedAsDataclass <https://docs.sqlalchemy.org/en/20/orm/dataclasses.html#orm-declarative-native-dataclasses>`__
    """  # noqa: E501

    __abstract__ = True


class Base(DataClassBase, DateTimeMixin):
    """
    Declarative Mixin data class base class, with data class integration, and contains MiXin data class basic table structure, you can simply understand it as a data class base class containing basic table structure
    """  # noqa: E501

    __abstract__ = True
