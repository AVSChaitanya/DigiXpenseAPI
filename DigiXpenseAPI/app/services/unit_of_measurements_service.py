#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select

from app.common.exception import errors
from app.crud.crud_unit_of_measurements import UnitofMeasurementsDao
from app.database.db_psql import async_db_session
from app.models.unit_of_measurements_model import PublicSTPUnitOfMeasurements
from app.schemas.unit_of_measurements import CreateUnitofMeasurement, UpdateUnitofMeasurement


class UnitofMeasurementsService:
    @staticmethod
    async def get(*, pk: int) -> PublicSTPUnitOfMeasurements:
        async with async_db_session() as db:
            api = await UnitofMeasurementsDao.get(db, RecId = pk)
            if not api:
                raise errors.NotFoundError(msg='Unit of Measurement with RecId does not exist')
            return api

    # @staticmethod
    # async def get_select(*, name: str = None, method: str = None, path: str = None) -> Select:
    #     return await FiscalYearGlobalDao.get_list(name=name, method=method, path=path)

    @staticmethod
    async def get_all() -> Sequence[PublicSTPUnitOfMeasurements]:
        async with async_db_session() as db:
            apis = await UnitofMeasurementsDao.get_all(db)
            return apis

    @staticmethod
    async def create(*, obj: CreateUnitofMeasurement) -> None:
        async with async_db_session.begin() as db:
            existing_UomId = await UnitofMeasurementsDao.get_by_UomId(db, obj.UomId)
            if existing_UomId:
                raise errors.ForbiddenError(msg='UomId already exists')

            existing_UomName = await UnitofMeasurementsDao.get_by_UomName(db, obj.UomName)
            if existing_UomName:
                raise errors.ForbiddenError(msg='UomName already exists')
            
            existing_UomSymbol = await UnitofMeasurementsDao.get_by_UomSymbol(db, obj.UomSymbol)
            if existing_UomSymbol:
                raise errors.ForbiddenError(msg='UomSymbol already exists')
            await UnitofMeasurementsDao.create(db, obj)

    @staticmethod
    async def update(*, RecId: int, obj: UpdateUnitofMeasurement) -> int:
        async with async_db_session.begin() as db:
            existing_UomId = await UnitofMeasurementsDao.get_by_UomId(db, obj.UomId)
            if existing_UomId:
                raise errors.ForbiddenError(msg='UomId already exists')

            existing_UomName = await UnitofMeasurementsDao.get_by_UomName(db, obj.UomName)
            if existing_UomName:
                raise errors.ForbiddenError(msg='UomName already exists')
            
            existing_UomSymbol = await UnitofMeasurementsDao.get_by_UomSymbol(db, obj.UomSymbol)
            if existing_UomSymbol:
                raise errors.ForbiddenError(msg='UomSymbol already exists')

            count = await UnitofMeasurementsDao.update(db, RecId, obj)
            return count

    @staticmethod
    async def delete(*, pk: list[int]) -> int:
        async with async_db_session.begin() as db:
            count = await UnitofMeasurementsDao.delete(db, pk)
            return count
