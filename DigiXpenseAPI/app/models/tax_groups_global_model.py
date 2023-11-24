from typing import List, Optional

from sqlalchemy import Boolean, Column, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, UniqueConstraint, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class PublicSTPGlobalCurrency(Base):
    __tablename__ = 'public.STPGlobalCurrency'
    __table_args__ = (
        PrimaryKeyConstraint('RecId', name='STPCurrencyGlobal_pk'),
        UniqueConstraint('CurrencyCode', name='public.STPGlobalCurrency_CurrencyCode_key'),
        UniqueConstraint('GlobalCurrencyId', name='public.STPGlobalCurrency_GlobalCurrencyId_key')
    )

    GlobalCurrencyId = mapped_column(String(100), nullable=False)
    CurrencyCode = mapped_column(String(30), nullable=False)
    RecId = mapped_column(Integer)
    GlobalCurrencyName = mapped_column(String(80))
    CurrencySymbol = mapped_column(String(10))
    CurrencyFormat = mapped_column(String(30))
    IsActive = mapped_column(Boolean, server_default=text('true'))

    public_STPCountries: Mapped[List['PublicSTPCountries']] = relationship('PublicSTPCountries', uselist=True, back_populates='public_STPGlobalCurrency')


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

    public_STPCountries: Mapped[List['PublicSTPCountries']] = relationship('PublicSTPCountries', uselist=True, back_populates='public_STPLanguageGlobal')


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

    public_STPCountries: Mapped[List['PublicSTPCountries']] = relationship('PublicSTPCountries', uselist=True, back_populates='public_STPTimezones')


class PublicSTPCountries(Base):
    __tablename__ = 'public.STPCountries'
    __table_args__ = (
        ForeignKeyConstraint(['DefaultCurrencyId'], ['public.STPGlobalCurrency.GlobalCurrencyId'], name='STPCountries_fk0'),
        ForeignKeyConstraint(['DefaultLanguageId'], ['public.STPLanguageGlobal.LanguageId'], name='STPCountries_fk1'),
        ForeignKeyConstraint(['DefaultTimezoneId'], ['public.STPTimezones.TimezoneId'], name='STPCountries_fk2'),
        PrimaryKeyConstraint('RecId', name='STPCountries_pk'),
        UniqueConstraint('CountryCode', name='public.STPCountries_CountryCode_key'),
        UniqueConstraint('CountryId', name='public.STPCountries_CountryId_key'),
        UniqueConstraint('CountryName', name='public.STPCountries_CountryName_key')
    )

    CountryId = mapped_column(String(30), nullable=False)
    CountryName = mapped_column(String(60), nullable=False)
    CountryCode = mapped_column(String(30), nullable=False)
    RecId = mapped_column(Integer)
    DefaultLanguageId = mapped_column(String(30))
    DefaultCurrencyId = mapped_column(String(30))
    DefaultTimezoneId = mapped_column(String(20))
    Capital = mapped_column(String(30))
    Region = mapped_column(String(50))
    FlagUrl = mapped_column(String(250))
    IsActive = mapped_column(Boolean, server_default=text('true'))

    public_STPGlobalCurrency: Mapped[Optional['PublicSTPGlobalCurrency']] = relationship('PublicSTPGlobalCurrency', back_populates='public_STPCountries')
    public_STPLanguageGlobal: Mapped[Optional['PublicSTPLanguageGlobal']] = relationship('PublicSTPLanguageGlobal', back_populates='public_STPCountries')
    public_STPTimezones: Mapped[Optional['PublicSTPTimezones']] = relationship('PublicSTPTimezones', back_populates='public_STPCountries')
    public_TAXTaxGroupsGlobal: Mapped[List['PublicTAXTaxGroupsGlobal']] = relationship('PublicTAXTaxGroupsGlobal', uselist=True, back_populates='public_STPCountries')


class PublicTAXTaxGroupsGlobal(Base):
    __tablename__ = 'public.TAXTaxGroupsGlobal'
    __table_args__ = (
        ForeignKeyConstraint(['Country'], ['public.STPCountries.CountryId'], name='TAXTaxGroupsGlobal_fk0'),
        PrimaryKeyConstraint('RecId', name='TAXTaxGroupsGlobal_pk'),
        UniqueConstraint('TaxGroup', name='public.TAXTaxGroupsGlobal_TaxGroup_key'),
        UniqueConstraint('TaxGroupId', name='public.TAXTaxGroupsGlobal_TaxGroupId_key')
    )

    TaxGroupId = mapped_column(String(20), nullable=False)
    TaxGroup = mapped_column(String(25), nullable=False)
    Description = mapped_column(String(250), nullable=False)
    Country = mapped_column(String(30), nullable=False)
    RecId = mapped_column(Integer)
    IsActive = mapped_column(Boolean, server_default=text('true'))

    public_STPCountries: Mapped['PublicSTPCountries'] = relationship('PublicSTPCountries', back_populates='public_TAXTaxGroupsGlobal')
