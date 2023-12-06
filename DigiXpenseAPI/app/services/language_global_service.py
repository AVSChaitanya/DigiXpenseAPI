#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select

from app.common.exception import errors
from app.crud.crud_language_global import LanguageGlobalDao
from app.database.db_psql import async_db_session
from app.models.language_global_model import PublicSTPLanguageGlobal
from app.schemas.language_global import CreateLanguageGlobal, UpdateLanguageGlobal


class LanguageGlobalService:
    @staticmethod
    async def get(*, pk: int) -> PublicSTPLanguageGlobal:
        async with async_db_session() as db:
            api = await LanguageGlobalDao.get(db, RecId = pk)
            if not api:
                raise errors.NotFoundError(msg='Language Global with RecId does not exist')
            return api

    # @staticmethod
    # async def get_select(*, name: str = None, method: str = None, path: str = None) -> Select:
    #     return await FiscalYearGlobalDao.get_list(name=name, method=method, path=path)

    @staticmethod
    async def get_all() -> Sequence[PublicSTPLanguageGlobal]:
        async with async_db_session() as db:
            apis = await LanguageGlobalDao.get_all(db)
            return apis

    @staticmethod
    async def create(*, obj: CreateLanguageGlobal) -> None:
        async with async_db_session.begin() as db:
            existing_ISO_Code = await LanguageGlobalDao.get_by_ISOCode(db, obj.ISOCode)
            if existing_ISO_Code:
                raise errors.ForbiddenError(msg='ISOCode already exists')

            existing_LanguageId = await LanguageGlobalDao.get_by_LanguageId(db, obj.LanguageId)
            if existing_LanguageId:
                raise errors.ForbiddenError(msg='LanguageId already exists')
            
            existing_LanguageName = await LanguageGlobalDao.get_by_LanguageName(db, obj.LanguageName)
            if existing_LanguageName:
                raise errors.ForbiddenError(msg='LanguageName already exists')
            await LanguageGlobalDao.create(db, obj)

    @staticmethod
    async def update(*, RecId: int, obj: UpdateLanguageGlobal) -> int:
        async with async_db_session.begin() as db:
            existing_ISO_Code = await LanguageGlobalDao.get_by_ISOCode(db, obj.ISOCode)
            if existing_ISO_Code:
                raise errors.ForbiddenError(msg='ISOCode already exists')

            existing_LanguageId = await LanguageGlobalDao.get_by_LanguageId(db, obj.LanguageId)
            if existing_LanguageId:
                raise errors.ForbiddenError(msg='LanguageId already exists')
            
            existing_LanguageName = await LanguageGlobalDao.get_by_LanguageName(db, obj.LanguageName)
            if existing_LanguageName:
                raise errors.ForbiddenError(msg='LanguageName already exists')
            count = await LanguageGlobalDao.update(db, RecId, obj)
            return count

    @staticmethod
    async def delete(*, pk: list[int]) -> int:
        async with async_db_session.begin() as db:
            count = await LanguageGlobalDao.delete(db, pk)
            return count
