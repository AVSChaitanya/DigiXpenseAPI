from typing import Sequence

from sqlalchemy import Select

from app.common.exception import errors
from app.crud.crud_fiscalyearglobal import FiscalYearGlobalDao
from app.database.db_psql import async_db_session
from app.models.fiscal_year_global_model import PublicSTPFiscalYearGlobal
from app.schemas.fiscalyear_global import CreateFiscalYearGlobal, UpdateFiscalYearGlobal


class FiscalYearGlobalService:
    @staticmethod
    async def get(*, pk: int) -> PublicSTPFiscalYearGlobal:
        async with async_db_session() as db:
            api = await FiscalYearGlobalDao.get(db, RecId = pk)
            if not api:
                raise errors.NotFoundError(msg='FiscalYear Global with RecId does not exist')
            return api

    # @staticmethod
    # async def get_select(*, name: str = None, method: str = None, path: str = None) -> Select:
    #     return await FiscalYearGlobalDao.get_list(name=name, method=method, path=path)

    @staticmethod
    async def get_all() -> Sequence[PublicSTPFiscalYearGlobal]:
        async with async_db_session() as db:
            apis = await FiscalYearGlobalDao.get_all(db)
            return apis

    @staticmethod
    async def create(*, obj: CreateFiscalYearGlobal) -> None:
        async with async_db_session.begin() as db:
            await FiscalYearGlobalDao.create(db, obj)

    @staticmethod
    async def update(*, RecId: int, obj: UpdateFiscalYearGlobal) -> int:
        async with async_db_session.begin() as db:
            count = await FiscalYearGlobalDao.update(db, RecId, obj)
            return count

    @staticmethod
    async def delete(*, pk: list[int]) -> int:
        async with async_db_session.begin() as db:
            count = await FiscalYearGlobalDao.delete(db, pk)
            return count
