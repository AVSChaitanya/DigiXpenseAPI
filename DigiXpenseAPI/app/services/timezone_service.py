#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select

from app.common.exception import errors
from app.crud.crud_timezones import TimezonesDao
from app.database.db_psql import async_db_session
from app.models.Timezones_model import PublicSTPTimezones
from app.schemas.timezones import CreateTimezone, UpdateTimezone


class TimezoneService:
    @staticmethod
    async def get(*, pk: int) -> PublicSTPTimezones:
        async with async_db_session() as db:
            api = await TimezonesDao.get(db, RecId = pk)
            if not api:
                raise errors.NotFoundError(msg='Timezone with RecId does not exist')
            return api

    # @staticmethod
    # async def get_select(*, name: str = None, method: str = None, path: str = None) -> Select:
    #     return await FiscalYearGlobalDao.get_list(name=name, method=method, path=path)

    @staticmethod
    async def get_all() -> Sequence[PublicSTPTimezones]:
        async with async_db_session() as db:
            apis = await TimezonesDao.get_all(db)
            return apis

    @staticmethod
    async def create(*, obj: CreateTimezone) -> None:
        async with async_db_session.begin() as db:
            existing_Timezone_Code = await TimezonesDao.get_by_TimezoneCode(db, obj.TimezoneCode)
            if existing_Timezone_Code:
                raise errors.ForbiddenError(msg='TimezoneCode already exists')

            existing_TimezoneId = await TimezonesDao.get_by_TimezoneId(db, obj.TimezoneId)
            if existing_TimezoneId:
                raise errors.ForbiddenError(msg='TimezoneId already exists')
            
            existing_TimezoneName = await TimezonesDao.get_by_TimezoneName(db, obj.TimezoneName)
            if existing_TimezoneName:
                raise errors.ForbiddenError(msg='TimezoneName already exists')
            await TimezonesDao.create(db, obj)

    @staticmethod
    async def update(*, RecId: int, obj: UpdateTimezone) -> int:
        async with async_db_session.begin() as db:
            existing_Timezone_Code = await TimezonesDao.get_by_TimezoneCode(db, obj.TimezoneCode)
            if existing_Timezone_Code:
                raise errors.ForbiddenError(msg='TimezoneCode already exists')

            existing_TimezoneId = await TimezonesDao.get_by_TimezoneId(db, obj.TimezoneId)
            if existing_TimezoneId:
                raise errors.ForbiddenError(msg='TimezoneId already exists')
            
            existing_TimezoneName = await TimezonesDao.get_by_TimezoneName(db, obj.TimezoneName)
            if existing_TimezoneName:
                raise errors.ForbiddenError(msg='TimezoneName already exists')
            count = await TimezonesDao.update(db, RecId, obj)
            return count

    @staticmethod
    async def delete(*, pk: list[int]) -> int:
        async with async_db_session.begin() as db:
            count = await TimezonesDao.delete(db, pk)
            return count
