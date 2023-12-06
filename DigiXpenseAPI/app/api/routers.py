from fastapi import APIRouter

from app.api.v1.fiscal_year_global import router as fiscal_year_router
from app.api.v1.global_currency import router as global_currency_router
from app.api.v1.language_global import router as language_global_router
from app.api.v1.timezones import router as timezones_router
from app.api.v1.unit_of_measurements import router as unit_of_measurement_router

from app.core.conf import settings

v1 = APIRouter(prefix=settings.API_V1_STR)

v1.include_router(fiscal_year_router, prefix='/fiscal year', tags=['Fiscal Year Global'])
v1.include_router(global_currency_router, prefix='/global currency', tags=['Global Currency'])
v1.include_router(language_global_router, prefix='/language global', tags=['Language Global'])
v1.include_router(timezones_router, prefix='/timezones', tags=['Timezones'])
v1.include_router(unit_of_measurement_router, prefix='/unit of measurement', tags=['Unit of Measurements'])