from pydantic import Field, validator
from app.schemas.base import SchemaBase

class GlobalCurrency(SchemaBase):
    GlobalCurrencyId : str = Field(..., description="Global Currency ID cannot be null")
    GlobalCurrencyName : str
    CurrencyCode : str = Field(..., description="CurrencyCode cannot be null")
    CurrencySymbol : str
    CurrencyFormat : str
    

class CreateGlobalCurrency(GlobalCurrency):
    pass


class UpdateGlobalCurrency(GlobalCurrency):
    pass


class GetAllGlobalCurrencies(GlobalCurrency):
    RecId: int = Field(..., description="RecId cannot be null")
    
    class Config:
        orm_mode = True
