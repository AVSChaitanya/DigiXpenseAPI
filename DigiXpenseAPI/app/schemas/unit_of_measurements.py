from pydantic import Field, validator
from app.schemas.base import SchemaBase

class UnitofMeasurements(SchemaBase):
    UomId : str = Field(..., description="Uom Id cannot be null")
    UomName : str =  Field(..., description="Uom Name cannot be null")
    UomSymbol : str
    UomCategory : str
    MeasurementSystem : str
   

class CreateUnitofMeasurement(UnitofMeasurements):
    pass


class UpdateUnitofMeasurement(UnitofMeasurements):
    pass


class GetAllUnitofMeasurements(UnitofMeasurements):
    RecId: int = Field(..., description="RecId cannot be null")
    
    class Config:
        orm_mode = True
