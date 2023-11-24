#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import math
from typing import TypeVar, Generic, Sequence, Dict, TYPE_CHECKING

from fastapi import Query, Depends
from fastapi_pagination import pagination_ctx
from fastapi_pagination.bases import AbstractPage, AbstractParams, RawParams
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination.links.bases import create_links
from pydantic import BaseModel
from pydantic.generics import GenericModel

if TYPE_CHECKING:
    from sqlalchemy import Select
    from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar('T')
DataT = TypeVar('DataT')
SchemaT = TypeVar('SchemaT')


class _Params(BaseModel, AbstractParams):
    page: int = Query(1, ge=1, description='Page number')
    size: int = Query(20, gt=0, le=100, description='Page size')  # Default 20 records

    def to_raw_params(self) -> RawParams:
        return RawParams(
            limit=self.size,
            offset=self.size * (self.page - 1),
        )


class _Page(AbstractPage[T], Generic[T]):
    items: Sequence[T]  # data
    total: int  # Total number of data
    page: int  # Page n
    size: int  # Quantity per page
    total_pages: int  # total pages
    links: Dict[str, str | None]  # 跳转链接

    __params_type__ = _Params  # Use custom Params

    @classmethod
    def create(
        cls,
        items: Sequence[T],
        total: int,
        params: _Params,
    ) -> _Page[T]:
        page = params.page
        size = params.size
        total_pages = math.ceil(total / params.size)
        links = create_links(
            **{
                'first': {'page': 1, 'size': f'{size}'},
                'last': {'page': f'{math.ceil(total / params.size)}', 'size': f'{size}'} if total > 0 else None,
                'next': {'page': f'{page + 1}', 'size': f'{size}'} if (page + 1) <= total_pages else None,
                'prev': {'page': f'{page - 1}', 'size': f'{size}'} if (page - 1) >= 1 else None,
            }
        ).dict()

        return cls(items=items, total=total, page=params.page, size=params.size, total_pages=total_pages, links=links)


class _PageData(GenericModel, Generic[DataT]):
    page_data: DataT | None = None


async def paging_data(db: AsyncSession, select: Select, page_data_schema: SchemaT) -> dict:
    """
    Create paginated data based on SQLAlchemy

    :param db:
    :param select:
    :param page_data_schema:
    :return:
    """
    _paginate = await paginate(db, select)
    page_data = _PageData[_Page[page_data_schema]](page_data=_paginate).dict()['page_data']
    return page_data


# Pagination dependency injection
PageDepends = Depends(pagination_ctx(_Page))
