from typing import Annotated

from fastapi import APIRouter, Query

# from SocialAnalytics.app.common.rbac import DependsRBAC
# from SocialAnalytics.app.common.jwt import DependsJwtAuth
from app.common.pagination import PageDepends, paging_data
from app.common.response.response_schema import response_base
from app.database.db_psql import CurrentSession
from app.schemas.fiscalyear_global import GetAllFiscalYearGlobal, CreateFiscalYearGlobal, UpdateFiscalYearGlobal
from app.services.fiscal_year_global_service import FiscalYearGlobalService

router = APIRouter()


@router.get('/all', summary='Get all interfaces')
async def get_all_apis():
    data = await FiscalYearGlobalService.get_all()
    return await response_base.success(data=data)


@router.get('/{RecId}', summary='Get interface details')
async def get_api(RecId: int):
    api = await FiscalYearGlobalService.get(pk=RecId)
    return await response_base.success(data=api)


# @router.get('', summary='（Fuzzy conditions) Get all interfaces in paging', dependencies=[PageDepends])
# async def get_api_list(
#     db: CurrentSession,
#     name: Annotated[str | None, Query()] = None,
#     method: Annotated[str | None, Query()] = None,
#     path: Annotated[str | None, Query()] = None,
# ):
#     api_select = await ApiService.get_select(name=name, method=method, path=path)
#     page_data = await paging_data(db, api_select, GetAllFiscalYearGlobal)
#     return await response_base.success(data=page_data)


@router.post('', summary='Create interface')
async def create_api(obj: CreateFiscalYearGlobal):
    await FiscalYearGlobalService.create(obj=obj)
    return await response_base.success()


@router.put('/{RecId}', summary='Update interface')
async def update_api(RecId: int, obj: UpdateFiscalYearGlobal):
    count = await FiscalYearGlobalService.update(pk=RecId, obj=obj)
    if count > 0:
        return await response_base.success()
    return await response_base.fail()


@router.delete('', summary='（Batch) Delete interfaces')
async def delete_api(pk: Annotated[list[int], Query(...)]):
    count = await FiscalYearGlobalService.delete(pk=pk)
    if count > 0:
        return await response_base.success()
    return await response_base.fail()
