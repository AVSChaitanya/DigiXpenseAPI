from typing import NoReturn, Sequence

from sqlalchemy import Select, select, desc, delete, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.fiscal_year_global_model import PublicSTPFiscalYearGlobal
from app.schemas.fiscalyear_global import CreateFiscalYearGlobal, UpdateFiscalYearGlobal


class CRUDFiscalYearGlobal(CRUDBase[PublicSTPFiscalYearGlobal, CreateFiscalYearGlobal, UpdateFiscalYearGlobal]):
    async def get(self, db: AsyncSession, RecId: int) -> PublicSTPFiscalYearGlobal | None:
        return await self.get_(db, pk=RecId)

    # async def get_list(self, name: str = None, method: str = None, path: str = None) -> Select:
    #     se = select(self.model).order_by(desc(self.model.created_time))
    #     where_list = []
    #     if name:
    #         where_list.append(self.model.name.like(f'%{name}%'))
    #     if method:
    #         where_list.append(self.model.method == method)
    #     if path:
    #         where_list.append(self.model.path.like(f'%{path}%', escape='/'))
    #     if where_list:
    #         se = se.where(and_(*where_list))
    #     return se

    async def get_all(self, db: AsyncSession) -> Sequence[PublicSTPFiscalYearGlobal]:
        apis = await db.execute(select(self.model))
        return apis.scalars().all()

    async def get_by_RecId(self, db: AsyncSession, RecId: int) -> PublicSTPFiscalYearGlobal | None:
        api = await db.execute(select(self.model).where(self.model.RecId == RecId))
        return api.scalars().first()

    async def create(self, db: AsyncSession, obj_in: CreateFiscalYearGlobal) -> NoReturn:
        await self.create_(db, obj_in)

    async def update(self, db: AsyncSession, RecId: int, obj_in: UpdateFiscalYearGlobal) -> int:
        return await self.update_(db, RecId, obj_in)

    async def delete(self, db: AsyncSession, pk: list[int]) -> int:
        apis = await db.execute(delete(self.model).where(self.model.id.in_(pk)))
        return apis.rowcount


FiscalYearGlobalDao: CRUDFiscalYearGlobal = CRUDFiscalYearGlobal(PublicSTPFiscalYearGlobal)
