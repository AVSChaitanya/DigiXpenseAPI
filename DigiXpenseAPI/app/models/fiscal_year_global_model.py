from sqlalchemy import Boolean, Column, Enum, Integer, PrimaryKeyConstraint, String, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class PublicSTPFiscalYearGlobal(Base):
    __tablename__ = 'public.STPFiscalYearGlobal'
    __table_args__ = (
        PrimaryKeyConstraint('RecId', name='STPFiscalYearGlobal_pk'),
    )

    yearStart = mapped_column(String(30), nullable=False)
    yearEnd = mapped_column(String(30), nullable=False)
    RecId = mapped_column(Integer)
    GlobalFiscalYearId = mapped_column(Enum('JAN-DEC', 'FEB-JAN', 'MAR-FEB', 'APR-MAR', 'MAY-APR', 'APR-MAY', 'MAY-JUN', 'JUN-JUL', 'JUL-AUG', 'AUG-SEP', 'SEP-OCT', 'OCT-NOV', 'NOV-DEC', 'DEC-JAN', name='globalfiscalyearid'))
    IsActive = mapped_column(Boolean, server_default=text('true'))
