from typing import NoReturn, Sequence

from sqlalchemy import Select, select, desc, delete, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.language_global_model import PublicSTPLanguageGlobal
from app.schemas.language_global import CreateLanguageGlobal, UpdateLanguageGlobal


class CRUDLanguageGlobal(CRUDBase[PublicSTPLanguageGlobal, CreateLanguageGlobal, UpdateLanguageGlobal]):
    async def get(self, db: AsyncSession, RecId: int) -> PublicSTPLanguageGlobal | None:
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

    async def get_all(self, db: AsyncSession) -> Sequence[PublicSTPLanguageGlobal]:
        apis = await db.execute(select(self.model))
        return apis.scalars().all()
    
    async def get_by_ISOCode(self, db: AsyncSession, ISOCode: str) -> PublicSTPLanguageGlobal | None:
        api = await db.execute(select(self.model).where(self.model.ISOCode == ISOCode))
        return api.scalars().first()
    
    async def get_by_LanguageId(self, db: AsyncSession, LanguageId: str) -> PublicSTPLanguageGlobal | None:
        api = await db.execute(select(self.model).where(self.model.LanguageId == LanguageId))
        return api.scalars().first()

    async def get_by_LanguageName(self, db: AsyncSession, LanguageName: str) -> PublicSTPLanguageGlobal | None:
        api = await db.execute(select(self.model).where(self.model.LanguageName == LanguageName))
        return api.scalars().first()

    async def create(self, db: AsyncSession, obj_in: CreateLanguageGlobal) -> NoReturn:
        await self.create_(db, obj_in)

    async def update(self, db: AsyncSession, RecId: int, obj_in: UpdateLanguageGlobal) -> int:
        return await self.update_(db, RecId, obj_in)

    async def delete(self, db: AsyncSession, pk: list[int]) -> int:
        apis = await db.execute(delete(self.model).where(self.model.id.in_(pk)))
        return apis.rowcount


LanguageGlobalDao: CRUDLanguageGlobal = CRUDLanguageGlobal(PublicSTPLanguageGlobal)
