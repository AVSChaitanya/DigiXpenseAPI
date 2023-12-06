from typing import NoReturn, Sequence

from sqlalchemy import Select, select, desc, delete, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.global_currency_model import PublicSTPGlobalCurrency
from app.schemas.global_currency import CreateGlobalCurrency, UpdateGlobalCurrency


class CRUDGlobalCurrency(CRUDBase[PublicSTPGlobalCurrency, CreateGlobalCurrency, UpdateGlobalCurrency]):
    async def get(self, db: AsyncSession, RecId: int) -> PublicSTPGlobalCurrency | None:
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

    async def get_all(self, db: AsyncSession) -> Sequence[PublicSTPGlobalCurrency]:
        apis = await db.execute(select(self.model))
        return apis.scalars().all()
    

    async def get_by_CurrencyCode(self, db: AsyncSession, CurrencyCode: str) -> PublicSTPGlobalCurrency | None:
        api = await db.execute(select(self.model).where(self.model.CurrencyCode == CurrencyCode))
        return api.scalars().first()
    
    
    async def get_by_GlobalCurrencyId(self, db: AsyncSession, GlobalCurrencyId: str) -> PublicSTPGlobalCurrency | None:
        api = await db.execute(select(self.model).where(self.model.GlobalCurrencyId == GlobalCurrencyId))
        return api.scalars().first()


    async def create(self, db: AsyncSession, obj_in: CreateGlobalCurrency) -> NoReturn:
        await self.create_(db, obj_in)


    async def update(self, db: AsyncSession, RecId: int, obj_in: UpdateGlobalCurrency) -> int:
        return await self.update_(db, RecId, obj_in)
    

    async def delete(self, db: AsyncSession, pk: list[int]) -> int:
        apis = await db.execute(delete(self.model).where(self.model.id.in_(pk)))
        return apis.rowcount


GlobalCurrencyDao: CRUDGlobalCurrency = CRUDGlobalCurrency(PublicSTPGlobalCurrency)
