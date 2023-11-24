from sqlalchemy import Boolean, Column, Integer, PrimaryKeyConstraint, String, UniqueConstraint, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class PublicSTPLanguageGlobal(Base):
    __tablename__ = 'public.STPLanguageGlobal'
    __table_args__ = (
        PrimaryKeyConstraint('RecId', name='STPLanguageGlobal_pk'),
        UniqueConstraint('ISOCode', name='public.STPLanguageGlobal_ISOCode_key'),
        UniqueConstraint('LanguageId', name='public.STPLanguageGlobal_LanguageId_key'),
        UniqueConstraint('LanguageName', name='public.STPLanguageGlobal_LanguageName_key')
    )

    LanguageId = mapped_column(String(20), nullable=False)
    LanguageName = mapped_column(String(30), nullable=False)
    ISOCode = mapped_column(String(30), nullable=False)
    RecId = mapped_column(Integer)
    IsActive = mapped_column(Boolean, server_default=text('true'))
