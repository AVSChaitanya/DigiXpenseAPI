#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select

from app.common.exception import errors
from app.crud.crud_global_currency import GlobalCurrencyDao
from app.database.db_psql import async_db_session
from app.models.global_currency_model import PublicSTPGlobalCurrency
from app.schemas.global_currency import CreateGlobalCurrency, UpdateGlobalCurrency


class GlobalCurrencyService:
    @staticmethod
    async def get(*, pk: int) -> PublicSTPGlobalCurrency:
        async with async_db_session() as db:
            api = await GlobalCurrencyDao.get(db, RecId = pk)
            if not api:
                raise errors.NotFoundError(msg='Global Currency with RecId does not exist')
            return api

    # @staticmethod
    # async def get_select(*, name: str = None, method: str = None, path: str = None) -> Select:
    #     return await FiscalYearGlobalDao.get_list(name=name, method=method, path=path)

    @staticmethod
    async def get_all() -> Sequence[PublicSTPGlobalCurrency]:
        async with async_db_session() as db:
            apis = await GlobalCurrencyDao.get_all(db)
            return apis

    @staticmethod
    async def create(*, obj: CreateGlobalCurrency) -> None:
        async with async_db_session.begin() as db:
            existing_currency_code = await GlobalCurrencyDao.get_by_CurrencyCode(db, obj.CurrencyCode)
            if existing_currency_code:
                raise errors.ForbiddenError(msg='Currency with the same code already exists')

            existing_currency_id = await GlobalCurrencyDao.get_by_GlobalCurrencyId(db, obj.GlobalCurrencyId)
            if existing_currency_id:
                raise errors.ForbiddenError(msg='Currency with the same ID already exists')
            await GlobalCurrencyDao.create(db, obj)

    @staticmethod
    async def update(*, RecId: int, obj: UpdateGlobalCurrency) -> int:
        async with async_db_session.begin() as db:
            existing_currency_code = await GlobalCurrencyDao.get_by_CurrencyCode(db, obj.CurrencyCode)
            if existing_currency_code:
                raise errors.ForbiddenError(msg='Currency with the same code already exists')

            existing_currency_id = await GlobalCurrencyDao.get_by_GlobalCurrencyId(db, obj.GlobalCurrencyId)
            if existing_currency_id:
                raise errors.ForbiddenError(msg='Currency with the same ID already exists')
            count = await GlobalCurrencyDao.update(db, RecId, obj)
            return count

    @staticmethod
    async def delete(*, pk: list[int]) -> int:
        async with async_db_session.begin() as db:
            count = await GlobalCurrencyDao.delete(db, pk)
            return count
