from sqlalchemy import Boolean, Column, Integer, PrimaryKeyConstraint, String, UniqueConstraint, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class PublicSTPExpenseTypes(Base):
    __tablename__ = 'public.STPExpenseTypes'
    __table_args__ = (
        PrimaryKeyConstraint('RecId', name='STPExpenseType_pk'),
        UniqueConstraint('ExpenseTypeId', name='public.STPExpenseTypes_ExpenseTypeId_key')
    )

    ExpenseTypeId = mapped_column(String(30), nullable=False)
    ExpenseType = mapped_column(String(30), nullable=False)
    ExpenseTypeDescription = mapped_column(String(250), nullable=False)
    RecId = mapped_column(Integer)
    IsActive = mapped_column(Boolean, server_default=text('true'))
