from typing import List, Optional

from sqlalchemy import Boolean, Column, Enum, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, UniqueConstraint, text
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
    public_STPOrganization: Mapped[List['PublicSTPOrganization']] = relationship('PublicSTPOrganization', uselist=True, back_populates='public_STPGlobalCurrency')


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
    public_STPOrganization: Mapped[List['PublicSTPOrganization']] = relationship('PublicSTPOrganization', uselist=True, back_populates='public_STPLanguageGlobal')


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
    public_STPOrganization: Mapped[List['PublicSTPOrganization']] = relationship('PublicSTPOrganization', uselist=True, back_populates='public_STPTimezones')


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
    public_STPOrganization: Mapped[List['PublicSTPOrganization']] = relationship('PublicSTPOrganization', uselist=True, back_populates='public_STPCountries')


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
    public_STPOrganization: Mapped[List['PublicSTPOrganization']] = relationship('PublicSTPOrganization', uselist=True, back_populates='public_TAXTaxGroupsGlobal')


class PublicSTPOrganization(Base):
    __tablename__ = 'public.STPOrganization'
    __table_args__ = (
        ForeignKeyConstraint(['CountryId'], ['public.STPCountries.CountryId'], name='STPOrganization_fk0'),
        ForeignKeyConstraint(['DefaultCurrency'], ['public.STPGlobalCurrency.GlobalCurrencyId'], name='STPOrganization_fk1'),
        ForeignKeyConstraint(['DefaultLanguageId'], ['public.STPLanguageGlobal.LanguageId'], name='STPOrganization_fk3'),
        ForeignKeyConstraint(['DefaultTimeZone'], ['public.STPTimezones.TimezoneId'], name='STPOrganization_fk2'),
        ForeignKeyConstraint(['TaxGroupId'], ['public.TAXTaxGroupsGlobal.TaxGroupId'], name='STPOrganization_fk4'),
        PrimaryKeyConstraint('RecId', name='STPOrganization_pk'),
        UniqueConstraint('OrganizationId', name='public.STPOrganization_OrganizationId_key'),
        UniqueConstraint('RegistrationNumber', name='public.STPOrganization_RegistrationNumber_key')
    )

    OrganizationId = mapped_column(Integer, nullable=False)
    OrganizationName = mapped_column(String(120), nullable=False)
    PrimaryContact = mapped_column(String(25), nullable=False)
    City = mapped_column(String(30), nullable=False)
    RegistrationNumber = mapped_column(String(20), nullable=False)
    CountryId = mapped_column(String(30), nullable=False)
    TaxGroupId = mapped_column(String(20), nullable=False)
    RecId = mapped_column(Integer)
    ParentOrganizationId = mapped_column(Integer)
    OrganizationType = mapped_column(Enum('Business', 'Individual', name='organizationtype'))
    Industries = mapped_column(Enum('Agriculture', 'Metal Production', 'Chemical Industry', 'Construction', 'Education', 'Financial Services', 'Professional Services', 'Food Industry', 'HealthCare Industry', 'public Services', 'Mining', 'Mechanical And Electical', 'Medical', 'Oil And Gas Industry', 'Postal And Telecom', 'Shipping/Transportation', 'Textiles/Clothing', 'Utilities', name='industries'))
    AddressLine1 = mapped_column(String(300))
    AddressLine2 = mapped_column(String(300))
    State = mapped_column(String(30))
    ZipCode = mapped_column(String(40))
    ContactName = mapped_column(String(120))
    EmailId = mapped_column(String(180))
    Website = mapped_column(String(180))
    PrimaryContactName = mapped_column(String(120))
    ContactFirstName = mapped_column(String(50))
    ContactMiddleName = mapped_column(String(50))
    ContactLastName = mapped_column(String(50))
    PrimaryContactEmailId = mapped_column(String(180))
    PrimaryContactNumber = mapped_column(String(20))
    PrimaryContactDesignation = mapped_column(String(60))
    BillingContactEmailId = mapped_column(String(180))
    BillingFirstName = mapped_column(String(50))
    BillingMiddleName = mapped_column(String(50))
    BillingLastName = mapped_column(String(50))
    BillingContactNumber = mapped_column(String(20))
    BillingContactDesignation = mapped_column(String(60))
    DefaultCurrency = mapped_column(String(30))
    DefaultTimeZone = mapped_column(String(20))
    DefaultLanguageId = mapped_column(String(20))
    DecimalSeperator = mapped_column(Enum('.', ',', name='decimalseperator'))
    ExchangeRateProvider = mapped_column(String(30))
    ShowAnalyticsOnList = mapped_column(Boolean, server_default=text('true'))
    DefaultPaymentMethodId = mapped_column(String(20))
    TaxId = mapped_column(String(60))
    AnnualRevenue = mapped_column(Numeric)
    CompanyRegistrationNo = mapped_column(String(45))
    IsActive = mapped_column(Boolean, server_default=text('true'))
    DefaultDateFormat = mapped_column(Enum('mm/dd/yyyy', 'dd/mm/yyyy', 'yyyy/mm/dd', 'mm-dd-yyyy', 'dd-mm-yyyy', 'yyyy-mm-dd', 'mm.dd.yyyy', 'dd.mm.yyyy', 'yyyy.mm.dd', 'MM/dd/yyyy', 'dd/MM/yyyy', 'yyyy/MM/dd', 'MM-dd-yyyy', 'dd-MM-yyyy', 'yyyy-MM-dd', 'MM.dd.yyyy', 'dd.MM.yyyy', 'yyyy.MM.dd', name='defaultdateformat'))

    public_STPCountries: Mapped['PublicSTPCountries'] = relationship('PublicSTPCountries', back_populates='public_STPOrganization')
    public_STPGlobalCurrency: Mapped[Optional['PublicSTPGlobalCurrency']] = relationship('PublicSTPGlobalCurrency', back_populates='public_STPOrganization')
    public_STPLanguageGlobal: Mapped[Optional['PublicSTPLanguageGlobal']] = relationship('PublicSTPLanguageGlobal', back_populates='public_STPOrganization')
    public_STPTimezones: Mapped[Optional['PublicSTPTimezones']] = relationship('PublicSTPTimezones', back_populates='public_STPOrganization')
    public_TAXTaxGroupsGlobal: Mapped['PublicTAXTaxGroupsGlobal'] = relationship('PublicTAXTaxGroupsGlobal', back_populates='public_STPOrganization')
    public_STPOrganizationDBConnectionDetails: Mapped[List['PublicSTPOrganizationDBConnectionDetails']] = relationship('PublicSTPOrganizationDBConnectionDetails', uselist=True, back_populates='public_STPOrganization')


class PublicSTPOrganizationDBConnectionDetails(Base):
    __tablename__ = 'public.STPOrganizationDBConnectionDetails'
    __table_args__ = (
        ForeignKeyConstraint(['OrganizationId'], ['public.STPOrganization.OrganizationId'], name='public.STPOrganizationDBConnectionDetails_OrganizationId_fkey'),
        PrimaryKeyConstraint('OrgDBId', name='public.STPOrganizationDBConnectionDetails_pkey')
    )

    OrgDBId = mapped_column(Integer)
    DatabaseType = mapped_column(String(250), nullable=False)
    DatabaseServer = mapped_column(String(500), nullable=False)
    OrganizationId = mapped_column(Integer)
    DatabaseName = mapped_column(String(250))
    DatabaseSchema = mapped_column(String(250))
    UserName = mapped_column(String(250))
    Password = mapped_column(String(250))

    public_STPOrganization: Mapped[Optional['PublicSTPOrganization']] = relationship('PublicSTPOrganization', back_populates='public_STPOrganizationDBConnectionDetails')
