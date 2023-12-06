from pydantic import Field, validator
from app.schemas.base import SchemaBase
from app.common.enums import GlobalFiscalYearId


class FiscalYearGlobal(SchemaBase):
    GlobalFiscalYearId : GlobalFiscalYearId
    yearStart: str = Field(..., description="yearStart cannot be null")
    yearEnd: str = Field(..., description="yearEnd cannot be null")
   

class CreateFiscalYearGlobal(FiscalYearGlobal):
    pass


class UpdateFiscalYearGlobal(FiscalYearGlobal):
    pass


class GetAllFiscalYearGlobal(FiscalYearGlobal):
    RecId: int = Field(..., description="RecId cannot be null")
    
    class Config:
        orm_mode = True