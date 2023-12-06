from typing import NoReturn, Sequence

from sqlalchemy import Select, select, desc, delete, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.Timezones_model import PublicSTPTimezones
from app.schemas.timezones import CreateTimezone, UpdateTimezone


class CRUDTimezones(CRUDBase[PublicSTPTimezones, CreateTimezone, UpdateTimezone]):
    async def get(self, db: AsyncSession, RecId: int) -> PublicSTPTimezones | None:
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

    async def get_all(self, db: AsyncSession) -> Sequence[PublicSTPTimezones]:
        apis = await db.execute(select(self.model))
        return apis.scalars().all()
    
    async def get_by_TimezoneCode(self, db: AsyncSession, TimezoneCode: str) -> PublicSTPTimezones | None:
        api = await db.execute(select(self.model).where(self.model.TimezoneCode == TimezoneCode))
        return api.scalars().first()

    async def get_by_TimezoneId(self, db: AsyncSession, TimezoneId: str) -> PublicSTPTimezones | None:
        api = await db.execute(select(self.model).where(self.model.TimezoneId == TimezoneId))
        return api.scalars().first()    

    async def get_by_TimezoneName(self, db: AsyncSession, TimezoneName: str) -> PublicSTPTimezones | None:
        api = await db.execute(select(self.model).where(self.model.TimezoneName == TimezoneName))
        return api.scalars().first()

    async def create(self, db: AsyncSession, obj_in: CreateTimezone) -> NoReturn:
        await self.create_(db, obj_in)

    async def update(self, db: AsyncSession, RecId: int, obj_in: UpdateTimezone) -> int:
        return await self.update_(db, RecId, obj_in)

    async def delete(self, db: AsyncSession, pk: list[int]) -> int:
        apis = await db.execute(delete(self.model).where(self.model.id.in_(pk)))
        return apis.rowcount


TimezonesDao: CRUDTimezones = CRUDTimezones(PublicSTPTimezones)
