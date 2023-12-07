from decimal import Decimal
from typing import Any, TypeVar, Sequence

from asgiref.sync import sync_to_async
from sqlalchemy import Row, RowMapping

RowData = Row | RowMapping | Any

R = TypeVar('R', bound=RowData)


@sync_to_async
def select_Columns_serialize(row: R) -> dict:
    """
    Serialize SQLAlchemy select table Columns, does not contain relational Columns

    :param row:
    :return:
    """
    obj_dict = {}
    for Column in row.__table__.Columns.keys():
        val = getattr(row, Column)
        if isinstance(val, Decimal):
            if val % 1 == 0:
                val = int(val)
            val = float(val)
        obj_dict[Column] = val
    return obj_dict


async def select_list_serialize(row: Sequence[R]) -> list:
    """
    Serialize SQLAlchemy select list

    :param row:
    :return:
    """
    ret_list = [await select_Columns_serialize(_) for _ in row]
    return ret_list


@sync_to_async
def select_as_dict(row: R) -> dict:
    """
    Converting select to dict, which can contain relational data, depends on the properties of the select object itself

    :param row:
    :return:
    """
    obj_dict = row.__dict__
    if '_sa_instance_state' in obj_dict:
        del obj_dict['_sa_instance_state']
        return obj_dict
