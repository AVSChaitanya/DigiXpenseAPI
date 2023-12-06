from sqlalchemy import Boolean, Column, Integer, PrimaryKeyConstraint, String, UniqueConstraint, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class PublicSTPTimezones(Base):
    __tablename__ = 'public.STPTimezones'
    __table_args__ = (
        PrimaryKeyConstraint('RecId', name='STPTimezones_pk'),
        UniqueConstraint('TimezoneCode', name='public.STPTimezones_TimezoneCode_key'),
        UniqueConstraint('TimezoneId', name='public.STPTimezones_TimezoneId_key'),
        UniqueConstraint('TimezoneName', name='public.STPTimezones_TimezoneName_key')
    )

    TimezoneId = mapped_column(String(20), nullable=False)
    RecId = mapped_column(Integer)
    TimezoneName = mapped_column(String(80))
    TimezoneCode = mapped_column(String(120))
    IsActive = mapped_column(Boolean, server_default=text('true'))

