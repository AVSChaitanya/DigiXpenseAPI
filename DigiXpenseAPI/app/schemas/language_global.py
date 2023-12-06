from pydantic import Field, validator
from app.schemas.base import SchemaBase

class LanguageGlobal(SchemaBase):
    LanguageId : str = Field(..., description="Language Id cannot be null")
    LanguageName : str = Field(..., description="Language Name cannot be null")
    ISOCode : str = Field(..., description="ISOCode cannot be null")
   

class CreateLanguageGlobal(LanguageGlobal):
    pass


class UpdateLanguageGlobal(LanguageGlobal):
    pass


class GetAllLanguageGlobal(LanguageGlobal):
    RecId: int = Field(..., description="RecId cannot be null")
    
    class Config:
        orm_mode = True
