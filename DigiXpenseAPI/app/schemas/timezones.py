from pydantic import Field, validator
from app.schemas.base import SchemaBase

class Timezones(SchemaBase):
    TimezoneId : str = Field(..., description="Timezone Id cannot be null")
    TimezoneName : str
    TimezoneCode : str
   

class CreateTimezone(Timezones):
    pass


class UpdateTimezone(Timezones):
    pass


class GetAllTimezones(Timezones):
    RecId: int = Field(..., description="RecId cannot be null")
    
    class Config:
        orm_mode = True
