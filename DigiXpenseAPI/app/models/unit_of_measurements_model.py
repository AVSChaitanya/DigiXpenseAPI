from sqlalchemy import Boolean, Column, Integer, PrimaryKeyConstraint, String, UniqueConstraint, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class PublicSTPUnitOfMeasurements(Base):
    __tablename__ = 'public.STPUnitOfMeasurements'
    __table_args__ = (
        PrimaryKeyConstraint('RecId', name='STPUnitOfMeasurements_pk'),
        UniqueConstraint('UomId', name='public.STPUnitOfMeasurements_UomId_key'),
        UniqueConstraint('UomName', name='public.STPUnitOfMeasurements_UomName_key'),
        UniqueConstraint('UomSymbol', name='public.STPUnitOfMeasurements_UomSymbol_key')
    )

    UomId = mapped_column(String(30), nullable=False)
    UomName = mapped_column(String(60), nullable=False)
    RecId = mapped_column(Integer)
    UomSymbol = mapped_column(String(10))
    UomCategory = mapped_column(String(20))
    MeasurementSystem = mapped_column(String(20))
    IsActive = mapped_column(Boolean, server_default=text('true'))
