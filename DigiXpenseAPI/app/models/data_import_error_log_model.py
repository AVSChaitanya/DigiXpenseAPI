from typing import List, Optional

from sqlalchemy import Boolean, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, Numeric, PrimaryKeyConstraint, String, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class PublicEMPEmployees(Base):
    __tablename__ = 'public.EMPEmployees'
    __table_args__ = (
        ForeignKeyConstraint(['BranchId'], ['public.STPCompanyBranches.BranchId'], name='EMPEmployees_fk10'),
        ForeignKeyConstraint(['CreatedBy'], ['public.SYSUsers.UserId'], name='EMPEmployees_fk5'),
        ForeignKeyConstraint(['DepartmentId'], ['public.STPDepartments.DepartmentId'], name='EMPEmployees_fk9'),
        ForeignKeyConstraint(['DimensionValueId'], ['public.STPDimensionValues.DimensionValueId'], name='EMPEmployees_fk3'),
        ForeignKeyConstraint(['FirstLineManager'], ['public.EMPEmployees.Id'], name='EMPEmployees_fk1'),
        ForeignKeyConstraint(['ModifiedBy'], ['public.SYSUsers.UserId'], name='EMPEmployees_fk6'),
        ForeignKeyConstraint(['OrganizationId'], ['public.STPOrganization.OrganizationId'], name='EMPEmployees_fk7'),
        ForeignKeyConstraint(['SecondLineManager'], ['public.EMPEmployees.Id'], name='EMPEmployees_fk2'),
        ForeignKeyConstraint(['SubOrganizationId'], ['public.STPOrganization.OrganizationId'], name='EMPEmployees_fk8'),
        PrimaryKeyConstraint('RecId', name='EMPEmployees_pk'),
        UniqueConstraint('ContactNumber', name='public.EMPEmployees_ContactNumber_key'),
        UniqueConstraint('Id', name='public.EMPEmployees_Id_key'),
        UniqueConstraint('OfficialEmail', name='public.EMPEmployees_OfficialEmail_key'),
        UniqueConstraint('PersonalEmail', name='public.EMPEmployees_PersonalEmail_key'),
        UniqueConstraint('ReferenceId', name='public.EMPEmployees_ReferenceId_key'),
        Index('Employees_Id_index', 'Id', 'OrganizationId', 'SubOrganizationId', unique=True)
    )

    Id = mapped_column(String(20), nullable=False)
    FirstName = mapped_column(String(60), nullable=False)
    LastName = mapped_column(String(60), nullable=False)
    EmploymentStartDate = mapped_column(Date, nullable=False)
    EmploymentEndDate = mapped_column(Date, nullable=False)
    DateOfBirth = mapped_column(Date, nullable=False)
    BranchId = mapped_column(String(20), nullable=False)
    OrganizationId = mapped_column(Integer, nullable=False)
    RecId = mapped_column(Integer)
    MiddleName = mapped_column(String(60))
    OfficialEmail = mapped_column(String(180))
    PersonalEmail = mapped_column(String(180))
    ContactNumber = mapped_column(String(20))
    DepartmentId = mapped_column(String(30))
    FirstLineManager = mapped_column(String(20))
    SecondLineManager = mapped_column(String(20))
    DimensionValueId = mapped_column(String(30))
    MaritalStatus = mapped_column(Enum('Married', 'Single', 'Widowed', 'Divorced', 'Cohabiting', 'Registered Partnership', 'Concubine', 'Separated', name='maritalstatus'))
    Gender = mapped_column(Enum('Male', 'Female', 'Non-Specific', name='gender'))
    EmploymentStatus = mapped_column(Enum('Active', 'Inactive', 'On Long Vacation', name='employmentstatus'))
    CreatedDatetime = mapped_column(DateTime)
    ModifiedDatetime = mapped_column(DateTime)
    ReferenceId = mapped_column(String(20))
    CreatedBy = mapped_column(String(20))
    ModifiedBy = mapped_column(String(20))
    IsActive = mapped_column(Boolean, server_default=text('true'))
    SubOrganizationId = mapped_column(Integer)

    public_STPCompanyBranches: Mapped['PublicSTPCompanyBranches'] = relationship('PublicSTPCompanyBranches', foreign_keys=[BranchId], back_populates='public_EMPEmployees')
    public_SYSUsers: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[CreatedBy], back_populates='public_EMPEmployees')
    public_STPDepartments: Mapped[Optional['PublicSTPDepartments']] = relationship('PublicSTPDepartments', foreign_keys=[DepartmentId], back_populates='public_EMPEmployees')
    public_STPDimensionValues: Mapped[Optional['PublicSTPDimensionValues']] = relationship('PublicSTPDimensionValues', back_populates='public_EMPEmployees')
    public_EMPEmployees: Mapped[Optional['PublicEMPEmployees']] = relationship('PublicEMPEmployees', remote_side=[RecId], foreign_keys=[FirstLineManager], back_populates='public_EMPEmployees_reverse')
    public_EMPEmployees_reverse: Mapped[List['PublicEMPEmployees']] = relationship('PublicEMPEmployees', uselist=True, remote_side=[FirstLineManager], foreign_keys=[FirstLineManager], back_populates='public_EMPEmployees')
    public_SYSUsers_: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[ModifiedBy], back_populates='public_EMPEmployees_')
    public_STPOrganization: Mapped['PublicSTPOrganization'] = relationship('PublicSTPOrganization', foreign_keys=[OrganizationId], back_populates='public_EMPEmployees')
    public_EMPEmployees_: Mapped[Optional['PublicEMPEmployees']] = relationship('PublicEMPEmployees', remote_side=[RecId], foreign_keys=[SecondLineManager], back_populates='public_EMPEmployees__reverse')
    public_EMPEmployees__reverse: Mapped[List['PublicEMPEmployees']] = relationship('PublicEMPEmployees', uselist=True, remote_side=[SecondLineManager], foreign_keys=[SecondLineManager], back_populates='public_EMPEmployees_')
    public_STPOrganization_: Mapped[Optional['PublicSTPOrganization']] = relationship('PublicSTPOrganization', foreign_keys=[SubOrganizationId], back_populates='public_EMPEmployees_')
    public_STPCompanyBranches_: Mapped[List['PublicSTPCompanyBranches']] = relationship('PublicSTPCompanyBranches', uselist=True, foreign_keys='[PublicSTPCompanyBranches.PrimaryContact]', back_populates='public_EMPEmployees_')
    public_STPDepartments_: Mapped[List['PublicSTPDepartments']] = relationship('PublicSTPDepartments', uselist=True, foreign_keys='[PublicSTPDepartments.PrimaryContact]', back_populates='public_EMPEmployees_')
    public_SYSUsers1: Mapped[List['PublicSYSUsers']] = relationship('PublicSYSUsers', uselist=True, foreign_keys='[PublicSYSUsers.EmployeeId]', back_populates='public_EMPEmployees1')


class PublicSTPCompanyBranches(Base):
    __tablename__ = 'public.STPCompanyBranches'
    __table_args__ = (
        ForeignKeyConstraint(['CountryId'], ['public.STPCountries.CountryId'], name='STPCompanyBranch_fk3'),
        ForeignKeyConstraint(['CreatedBy'], ['public.SYSUsers.UserId'], name='STPCompanyBranch_fk4'),
        ForeignKeyConstraint(['ModifiedBy'], ['public.SYSUsers.UserId'], name='STPCompanyBranch_fk5'),
        ForeignKeyConstraint(['OrganizationId'], ['public.STPOrganization.OrganizationId'], name='STPCompanyBranch_fk6'),
        ForeignKeyConstraint(['PrimaryContact'], ['public.EMPEmployees.Id'], name='STPCompanyBranch_fk0'),
        ForeignKeyConstraint(['StateId'], ['public.STPStates.StateId'], name='STPCompanyBranch_fk2'),
        ForeignKeyConstraint(['SubOrganizationId'], ['public.STPOrganization.OrganizationId'], name='STPCompanyBranch_fk7'),
        PrimaryKeyConstraint('RecId', name='STPCompanyBranch_pk'),
        UniqueConstraint('BranchId', name='public.STPCompanyBranches_BranchId_key'),
        UniqueConstraint('BranchName', name='public.STPCompanyBranches_BranchName_key'),
        Index('CompanyBranches_BranchId_index', 'BranchId', 'OrganizationId', 'SubOrganizationId', unique=True)
    )

    BranchId = mapped_column(String(20), nullable=False)
    BranchName = mapped_column(String(20), nullable=False)
    PrimaryContact = mapped_column(String(20), nullable=False)
    City = mapped_column(String(60), nullable=False)
    CountryId = mapped_column(String(30), nullable=False)
    OrganizationId = mapped_column(Integer, nullable=False)
    RecId = mapped_column(Integer)
    AddressLine1 = mapped_column(String(300))
    AddressLine2 = mapped_column(String(300))
    StateId = mapped_column(String(30))
    PostalCode = mapped_column(String(15))
    TaxNo = mapped_column(String(30))
    BranchAdmins = mapped_column(Text)
    CreatedDatetime = mapped_column(DateTime)
    ModifiedDatetime = mapped_column(DateTime)
    CreatedBy = mapped_column(String(20))
    ModifiedBy = mapped_column(String(20))
    IsActive = mapped_column(Boolean, server_default=text('true'))
    IsPrimary = mapped_column(Boolean, server_default=text('true'))
    SubOrganizationId = mapped_column(Integer)

    public_EMPEmployees: Mapped[List['PublicEMPEmployees']] = relationship('PublicEMPEmployees', uselist=True, foreign_keys='[PublicEMPEmployees.BranchId]', back_populates='public_STPCompanyBranches')
    public_STPCountries: Mapped['PublicSTPCountries'] = relationship('PublicSTPCountries', back_populates='public_STPCompanyBranches')
    public_SYSUsers: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[CreatedBy], back_populates='public_STPCompanyBranches')
    public_SYSUsers_: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[ModifiedBy], back_populates='public_STPCompanyBranches_')
    public_STPOrganization: Mapped['PublicSTPOrganization'] = relationship('PublicSTPOrganization', foreign_keys=[OrganizationId], back_populates='public_STPCompanyBranches')
    public_EMPEmployees_: Mapped['PublicEMPEmployees'] = relationship('PublicEMPEmployees', foreign_keys=[PrimaryContact], back_populates='public_STPCompanyBranches_')
    public_STPStates: Mapped[Optional['PublicSTPStates']] = relationship('PublicSTPStates', back_populates='public_STPCompanyBranches')
    public_STPOrganization_: Mapped[Optional['PublicSTPOrganization']] = relationship('PublicSTPOrganization', foreign_keys=[SubOrganizationId], back_populates='public_STPCompanyBranches_')


class PublicSTPDepartments(Base):
    __tablename__ = 'public.STPDepartments'
    __table_args__ = (
        ForeignKeyConstraint(['CreatedBy'], ['public.SYSUsers.UserId'], name='STPDepartments_fk1'),
        ForeignKeyConstraint(['ModifiedBy'], ['public.SYSUsers.UserId'], name='STPDepartments_fk2'),
        ForeignKeyConstraint(['OrganizationId'], ['public.STPOrganization.OrganizationId'], name='STPDepartments_fk3'),
        ForeignKeyConstraint(['PrimaryContact'], ['public.EMPEmployees.Id'], name='STPDepartments_fk0'),
        ForeignKeyConstraint(['SubOrganizationId'], ['public.STPOrganization.OrganizationId'], name='STPDepartments_fk4'),
        PrimaryKeyConstraint('RecId', name='STPDepartments_pk'),
        UniqueConstraint('DepartmentId', name='public.STPDepartments_DepartmentId_key'),
        UniqueConstraint('DepartmentName', name='public.STPDepartments_DepartmentName_key'),
        Index('Departments_DepartmentId_index', 'DepartmentId', 'OrganizationId', 'SubOrganizationId', unique=True)
    )

    DepartmentId = mapped_column(String(30), nullable=False)
    DepartmentName = mapped_column(String(30), nullable=False)
    Description = mapped_column(String(250), nullable=False)
    OrganizationId = mapped_column(Integer, nullable=False)
    RecId = mapped_column(Integer)
    DepartmentAdmins = mapped_column(Text)
    PrimaryContact = mapped_column(String(20))
    CreatedDatetime = mapped_column(DateTime)
    CreatedBy = mapped_column(String(20))
    ModifiedDatetime = mapped_column(DateTime)
    ModifiedBy = mapped_column(String(20))
    IsActive = mapped_column(Boolean, server_default=text('true'))
    SubOrganizationId = mapped_column(Integer)

    public_EMPEmployees: Mapped[List['PublicEMPEmployees']] = relationship('PublicEMPEmployees', uselist=True, foreign_keys='[PublicEMPEmployees.DepartmentId]', back_populates='public_STPDepartments')
    public_SYSUsers: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[CreatedBy], back_populates='public_STPDepartments')
    public_SYSUsers_: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[ModifiedBy], back_populates='public_STPDepartments_')
    public_STPOrganization: Mapped['PublicSTPOrganization'] = relationship('PublicSTPOrganization', foreign_keys=[OrganizationId], back_populates='public_STPDepartments')
    public_EMPEmployees_: Mapped[Optional['PublicEMPEmployees']] = relationship('PublicEMPEmployees', foreign_keys=[PrimaryContact], back_populates='public_STPDepartments_')
    public_STPOrganization_: Mapped[Optional['PublicSTPOrganization']] = relationship('PublicSTPOrganization', foreign_keys=[SubOrganizationId], back_populates='public_STPDepartments_')


class PublicSTPDimensionValues(Base):
    __tablename__ = 'public.STPDimensionValues'
    __table_args__ = (
        ForeignKeyConstraint(['CreatedBy'], ['public.SYSUsers.UserId'], name='STPDimensionValues_fk1'),
        ForeignKeyConstraint(['DimensionId'], ['public.STPDimensions.DimensionId'], name='STPDimensionValues_fk0'),
        ForeignKeyConstraint(['ModifiedBy'], ['public.SYSUsers.UserId'], name='STPDimensionValues_fk2'),
        ForeignKeyConstraint(['OrganizationId'], ['public.STPOrganization.OrganizationId'], name='STPDimensionValues_fk3'),
        ForeignKeyConstraint(['SubOrganizationId'], ['public.STPOrganization.OrganizationId'], name='STPDimensionValues_fk4'),
        PrimaryKeyConstraint('RecId', name='STPDimensionValues_pk'),
        UniqueConstraint('DimensionValueId', name='public.STPDimensionValues_DimensionValueId_key'),
        UniqueConstraint('ValueName', name='public.STPDimensionValues_ValueName_key'),
        Index('DimensionValues_DimensionId_index', 'DimensionId', 'OrganizationId', 'SubOrganizationId')
    )

    DimensionId = mapped_column(String(20), nullable=False)
    ValueName = mapped_column(String(30), nullable=False)
    OrganizationId = mapped_column(Integer, nullable=False)
    RecId = mapped_column(Integer)
    DimensionValueId = mapped_column(String(20), server_default=text("('DVI-'::text || (nextval('dimensionvalues_id_seq'::regclass))::text)"))
    Description = mapped_column(String(120))
    CreatedDatetime = mapped_column(DateTime)
    CreatedBy = mapped_column(String(20))
    ModifiedDatetime = mapped_column(DateTime)
    ModifiedBy = mapped_column(String(20))
    IsActive = mapped_column(Boolean, server_default=text('true'))
    SubOrganizationId = mapped_column(Integer)

    public_EMPEmployees: Mapped[List['PublicEMPEmployees']] = relationship('PublicEMPEmployees', uselist=True, back_populates='public_STPDimensionValues')
    public_SYSUsers: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[CreatedBy], back_populates='public_STPDimensionValues')
    public_STPDimensions: Mapped['PublicSTPDimensions'] = relationship('PublicSTPDimensions', back_populates='public_STPDimensionValues')
    public_SYSUsers_: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[ModifiedBy], back_populates='public_STPDimensionValues_')
    public_STPOrganization: Mapped['PublicSTPOrganization'] = relationship('PublicSTPOrganization', foreign_keys=[OrganizationId], back_populates='public_STPDimensionValues')
    public_STPOrganization_: Mapped[Optional['PublicSTPOrganization']] = relationship('PublicSTPOrganization', foreign_keys=[SubOrganizationId], back_populates='public_STPDimensionValues_')


class PublicSTPDimensions(Base):
    __tablename__ = 'public.STPDimensions'
    __table_args__ = (
        ForeignKeyConstraint(['CreatedBy'], ['public.SYSUsers.UserId'], name='STPDimensions_fk0'),
        ForeignKeyConstraint(['ModifiedBy'], ['public.SYSUsers.UserId'], name='STPDimensions_fk1'),
        ForeignKeyConstraint(['OrganizationId'], ['public.STPOrganization.OrganizationId'], name='STPDimensions_fk2'),
        ForeignKeyConstraint(['SubOrganizationId'], ['public.STPOrganization.OrganizationId'], name='STPDimensions_fk3'),
        PrimaryKeyConstraint('RecId', name='STPDimensions_pk'),
        UniqueConstraint('DimensionId', name='public.STPDimensions_DimensionId_key'),
        UniqueConstraint('DimensionName', name='public.STPDimensions_DimensionName_key'),
        Index('Dimensions_DimensionId_index', 'DimensionId', 'OrganizationId', 'SubOrganizationId', unique=True)
    )

    DimensionId = mapped_column(String(20), nullable=False)
    DimensionName = mapped_column(String(30), nullable=False)
    Description = mapped_column(String(250), nullable=False)
    OrganizationId = mapped_column(Integer, nullable=False)
    RecId = mapped_column(Integer)
    DimensionType = mapped_column(Enum('System', 'Custom', name='dimensiontype'))
    UseValuesFrom = mapped_column(Enum('Departments', 'Branches', 'Projects', 'Employees', 'ExpenseCategories', 'Vendors', name='usevaluesfrom'))
    CreatedDatetime = mapped_column(DateTime)
    CreatedBy = mapped_column(String(20))
    ModifiedDatetime = mapped_column(DateTime)
    ModifiedBy = mapped_column(String(20))
    EffectiveFrom = mapped_column(Date)
    EffectiveTo = mapped_column(Date)
    SubOrganizationId = mapped_column(Integer)

    public_STPDimensionValues: Mapped[List['PublicSTPDimensionValues']] = relationship('PublicSTPDimensionValues', uselist=True, back_populates='public_STPDimensions')
    public_SYSUsers: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[CreatedBy], back_populates='public_STPDimensions')
    public_SYSUsers_: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[ModifiedBy], back_populates='public_STPDimensions_')
    public_STPOrganization: Mapped['PublicSTPOrganization'] = relationship('PublicSTPOrganization', foreign_keys=[OrganizationId], back_populates='public_STPDimensions')
    public_STPOrganization_: Mapped[Optional['PublicSTPOrganization']] = relationship('PublicSTPOrganization', foreign_keys=[SubOrganizationId], back_populates='public_STPDimensions_')


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


class PublicSTPStates(Base):
    __tablename__ = 'public.STPStates'
    __table_args__ = (
        ForeignKeyConstraint(['CreatedBy'], ['public.SYSUsers.UserId'], name='STPStates_fk1'),
        ForeignKeyConstraint(['ModifiedBy'], ['public.SYSUsers.UserId'], name='STPStates_fk2'),
        ForeignKeyConstraint(['OrganizationId'], ['public.STPOrganization.OrganizationId'], name='STPStates_fk3'),
        ForeignKeyConstraint(['SubOrganizationId'], ['public.STPOrganization.OrganizationId'], name='STPStates_fk4'),
        PrimaryKeyConstraint('RecId', name='STPStates_pk'),
        UniqueConstraint('StateId', name='public.STPStates_StateId_key')
    )

    CountryId = mapped_column(String(30), nullable=False)
    RecId = mapped_column(Integer)
    StateId = mapped_column(String(30))
    CreatedDatetime = mapped_column(DateTime)
    ModifiedDatetime = mapped_column(DateTime)
    CreatedBy = mapped_column(String(20))
    ModifiedBy = mapped_column(String(20))
    IsActive = mapped_column(Boolean, server_default=text('true'))
    OrganizationId = mapped_column(Integer)
    SubOrganizationId = mapped_column(Integer)
    StateName = mapped_column(String(100))

    public_STPCompanyBranches: Mapped[List['PublicSTPCompanyBranches']] = relationship('PublicSTPCompanyBranches', uselist=True, back_populates='public_STPStates')
    public_SYSUsers: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[CreatedBy], back_populates='public_STPStates')
    public_SYSUsers_: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[ModifiedBy], back_populates='public_STPStates_')
    public_STPOrganization: Mapped[Optional['PublicSTPOrganization']] = relationship('PublicSTPOrganization', foreign_keys=[OrganizationId], back_populates='public_STPStates')
    public_STPOrganization_: Mapped[Optional['PublicSTPOrganization']] = relationship('PublicSTPOrganization', foreign_keys=[SubOrganizationId], back_populates='public_STPStates_')


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


class PublicSYSUsers(Base):
    __tablename__ = 'public.SYSUsers'
    __table_args__ = (
        ForeignKeyConstraint(['CreatedBy'], ['public.SYSUsers.UserId'], name='SYSUsers_fk1'),
        ForeignKeyConstraint(['EmployeeId'], ['public.EMPEmployees.Id'], name='SYSUsers_fkEmployeeId'),
        ForeignKeyConstraint(['ModifiedBy'], ['public.SYSUsers.UserId'], name='SYSUsers_fk2'),
        ForeignKeyConstraint(['OrganizationId'], ['public.STPOrganization.OrganizationId'], name='SYSUsers_fk3'),
        ForeignKeyConstraint(['SubOrganizationId'], ['public.STPOrganization.OrganizationId'], name='SYSUsers_fk4'),
        PrimaryKeyConstraint('RecId', name='SYSUsers_pk'),
        UniqueConstraint('UserId', name='public.SYSUsers_UserId_key'),
        Index('Users_EmployeeId_index', 'EmployeeId', 'OrganizationId', 'SubOrganizationId', unique=True),
        Index('Users_UserId_index', 'UserId', 'OrganizationId', 'SubOrganizationId', unique=True)
    )

    UserId = mapped_column(String(20), nullable=False)
    Username = mapped_column(String(30), nullable=False)
    PasswordHash = mapped_column(String(60), nullable=False)
    OrganizationId = mapped_column(Integer, nullable=False)
    RecId = mapped_column(Integer)
    Email = mapped_column(String(300))
    CreatedBy = mapped_column(String(20))
    CreatedDatetime = mapped_column(DateTime)
    ModifiedBy = mapped_column(String(20))
    ModifiedDatetime = mapped_column(DateTime)
    Status = mapped_column(Enum('Created', 'Sent Invitation', 'Resent Invitation', 'Registered', 'Password Reset', name='status'))
    TourStatus = mapped_column(Enum('Active', 'Completed', 'Requested', name='tourstatus'))
    IsSuperAdmin = mapped_column(Boolean, server_default=text('false'))
    IsActive = mapped_column(Boolean, server_default=text('true'))
    SubOrganizationId = mapped_column(Integer)
    EmployeeId = mapped_column(String(20))

    public_EMPEmployees: Mapped[List['PublicEMPEmployees']] = relationship('PublicEMPEmployees', uselist=True, foreign_keys='[PublicEMPEmployees.CreatedBy]', back_populates='public_SYSUsers')
    public_EMPEmployees_: Mapped[List['PublicEMPEmployees']] = relationship('PublicEMPEmployees', uselist=True, foreign_keys='[PublicEMPEmployees.ModifiedBy]', back_populates='public_SYSUsers_')
    public_STPCompanyBranches: Mapped[List['PublicSTPCompanyBranches']] = relationship('PublicSTPCompanyBranches', uselist=True, foreign_keys='[PublicSTPCompanyBranches.CreatedBy]', back_populates='public_SYSUsers')
    public_STPCompanyBranches_: Mapped[List['PublicSTPCompanyBranches']] = relationship('PublicSTPCompanyBranches', uselist=True, foreign_keys='[PublicSTPCompanyBranches.ModifiedBy]', back_populates='public_SYSUsers_')
    public_STPDepartments: Mapped[List['PublicSTPDepartments']] = relationship('PublicSTPDepartments', uselist=True, foreign_keys='[PublicSTPDepartments.CreatedBy]', back_populates='public_SYSUsers')
    public_STPDepartments_: Mapped[List['PublicSTPDepartments']] = relationship('PublicSTPDepartments', uselist=True, foreign_keys='[PublicSTPDepartments.ModifiedBy]', back_populates='public_SYSUsers_')
    public_STPDimensionValues: Mapped[List['PublicSTPDimensionValues']] = relationship('PublicSTPDimensionValues', uselist=True, foreign_keys='[PublicSTPDimensionValues.CreatedBy]', back_populates='public_SYSUsers')
    public_STPDimensionValues_: Mapped[List['PublicSTPDimensionValues']] = relationship('PublicSTPDimensionValues', uselist=True, foreign_keys='[PublicSTPDimensionValues.ModifiedBy]', back_populates='public_SYSUsers_')
    public_STPDimensions: Mapped[List['PublicSTPDimensions']] = relationship('PublicSTPDimensions', uselist=True, foreign_keys='[PublicSTPDimensions.CreatedBy]', back_populates='public_SYSUsers')
    public_STPDimensions_: Mapped[List['PublicSTPDimensions']] = relationship('PublicSTPDimensions', uselist=True, foreign_keys='[PublicSTPDimensions.ModifiedBy]', back_populates='public_SYSUsers_')
    public_STPStates: Mapped[List['PublicSTPStates']] = relationship('PublicSTPStates', uselist=True, foreign_keys='[PublicSTPStates.CreatedBy]', back_populates='public_SYSUsers')
    public_STPStates_: Mapped[List['PublicSTPStates']] = relationship('PublicSTPStates', uselist=True, foreign_keys='[PublicSTPStates.ModifiedBy]', back_populates='public_SYSUsers_')
    public_SYSUsers: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', remote_side=[RecId], foreign_keys=[CreatedBy], back_populates='public_SYSUsers_reverse')
    public_SYSUsers_reverse: Mapped[List['PublicSYSUsers']] = relationship('PublicSYSUsers', uselist=True, remote_side=[CreatedBy], foreign_keys=[CreatedBy], back_populates='public_SYSUsers')
    public_EMPEmployees1: Mapped[Optional['PublicEMPEmployees']] = relationship('PublicEMPEmployees', foreign_keys=[EmployeeId], back_populates='public_SYSUsers1')
    public_SYSUsers_: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', remote_side=[RecId], foreign_keys=[ModifiedBy], back_populates='public_SYSUsers__reverse')
    public_SYSUsers__reverse: Mapped[List['PublicSYSUsers']] = relationship('PublicSYSUsers', uselist=True, remote_side=[ModifiedBy], foreign_keys=[ModifiedBy], back_populates='public_SYSUsers_')
    public_STPOrganization: Mapped['PublicSTPOrganization'] = relationship('PublicSTPOrganization', foreign_keys=[OrganizationId], back_populates='public_SYSUsers')
    public_STPOrganization_: Mapped[Optional['PublicSTPOrganization']] = relationship('PublicSTPOrganization', foreign_keys=[SubOrganizationId], back_populates='public_SYSUsers_')
    public_SYSDataImportTaskLog: Mapped[List['PublicSYSDataImportTaskLog']] = relationship('PublicSYSDataImportTaskLog', uselist=True, foreign_keys='[PublicSYSDataImportTaskLog.CreatedBy]', back_populates='public_SYSUsers')
    public_SYSDataImportTaskLog_: Mapped[List['PublicSYSDataImportTaskLog']] = relationship('PublicSYSDataImportTaskLog', uselist=True, foreign_keys='[PublicSYSDataImportTaskLog.ModifiedBy]', back_populates='public_SYSUsers_')
    public_SYSDataImportErrorLog: Mapped[List['PublicSYSDataImportErrorLog']] = relationship('PublicSYSDataImportErrorLog', uselist=True, foreign_keys='[PublicSYSDataImportErrorLog.CreatedBy]', back_populates='public_SYSUsers')
    public_SYSDataImportErrorLog_: Mapped[List['PublicSYSDataImportErrorLog']] = relationship('PublicSYSDataImportErrorLog', uselist=True, foreign_keys='[PublicSYSDataImportErrorLog.ModifiedBy]', back_populates='public_SYSUsers_')


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

    public_STPCompanyBranches: Mapped[List['PublicSTPCompanyBranches']] = relationship('PublicSTPCompanyBranches', uselist=True, back_populates='public_STPCountries')
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

    public_EMPEmployees: Mapped[List['PublicEMPEmployees']] = relationship('PublicEMPEmployees', uselist=True, foreign_keys='[PublicEMPEmployees.OrganizationId]', back_populates='public_STPOrganization')
    public_EMPEmployees_: Mapped[List['PublicEMPEmployees']] = relationship('PublicEMPEmployees', uselist=True, foreign_keys='[PublicEMPEmployees.SubOrganizationId]', back_populates='public_STPOrganization_')
    public_STPCompanyBranches: Mapped[List['PublicSTPCompanyBranches']] = relationship('PublicSTPCompanyBranches', uselist=True, foreign_keys='[PublicSTPCompanyBranches.OrganizationId]', back_populates='public_STPOrganization')
    public_STPCompanyBranches_: Mapped[List['PublicSTPCompanyBranches']] = relationship('PublicSTPCompanyBranches', uselist=True, foreign_keys='[PublicSTPCompanyBranches.SubOrganizationId]', back_populates='public_STPOrganization_')
    public_STPDepartments: Mapped[List['PublicSTPDepartments']] = relationship('PublicSTPDepartments', uselist=True, foreign_keys='[PublicSTPDepartments.OrganizationId]', back_populates='public_STPOrganization')
    public_STPDepartments_: Mapped[List['PublicSTPDepartments']] = relationship('PublicSTPDepartments', uselist=True, foreign_keys='[PublicSTPDepartments.SubOrganizationId]', back_populates='public_STPOrganization_')
    public_STPDimensionValues: Mapped[List['PublicSTPDimensionValues']] = relationship('PublicSTPDimensionValues', uselist=True, foreign_keys='[PublicSTPDimensionValues.OrganizationId]', back_populates='public_STPOrganization')
    public_STPDimensionValues_: Mapped[List['PublicSTPDimensionValues']] = relationship('PublicSTPDimensionValues', uselist=True, foreign_keys='[PublicSTPDimensionValues.SubOrganizationId]', back_populates='public_STPOrganization_')
    public_STPDimensions: Mapped[List['PublicSTPDimensions']] = relationship('PublicSTPDimensions', uselist=True, foreign_keys='[PublicSTPDimensions.OrganizationId]', back_populates='public_STPOrganization')
    public_STPDimensions_: Mapped[List['PublicSTPDimensions']] = relationship('PublicSTPDimensions', uselist=True, foreign_keys='[PublicSTPDimensions.SubOrganizationId]', back_populates='public_STPOrganization_')
    public_STPStates: Mapped[List['PublicSTPStates']] = relationship('PublicSTPStates', uselist=True, foreign_keys='[PublicSTPStates.OrganizationId]', back_populates='public_STPOrganization')
    public_STPStates_: Mapped[List['PublicSTPStates']] = relationship('PublicSTPStates', uselist=True, foreign_keys='[PublicSTPStates.SubOrganizationId]', back_populates='public_STPOrganization_')
    public_SYSUsers: Mapped[List['PublicSYSUsers']] = relationship('PublicSYSUsers', uselist=True, foreign_keys='[PublicSYSUsers.OrganizationId]', back_populates='public_STPOrganization')
    public_SYSUsers_: Mapped[List['PublicSYSUsers']] = relationship('PublicSYSUsers', uselist=True, foreign_keys='[PublicSYSUsers.SubOrganizationId]', back_populates='public_STPOrganization_')
    public_STPCountries: Mapped['PublicSTPCountries'] = relationship('PublicSTPCountries', back_populates='public_STPOrganization')
    public_STPGlobalCurrency: Mapped[Optional['PublicSTPGlobalCurrency']] = relationship('PublicSTPGlobalCurrency', back_populates='public_STPOrganization')
    public_STPLanguageGlobal: Mapped[Optional['PublicSTPLanguageGlobal']] = relationship('PublicSTPLanguageGlobal', back_populates='public_STPOrganization')
    public_STPTimezones: Mapped[Optional['PublicSTPTimezones']] = relationship('PublicSTPTimezones', back_populates='public_STPOrganization')
    public_TAXTaxGroupsGlobal: Mapped['PublicTAXTaxGroupsGlobal'] = relationship('PublicTAXTaxGroupsGlobal', back_populates='public_STPOrganization')
    public_SYSDataImportTaskLog: Mapped[List['PublicSYSDataImportTaskLog']] = relationship('PublicSYSDataImportTaskLog', uselist=True, foreign_keys='[PublicSYSDataImportTaskLog.OrganizationId]', back_populates='public_STPOrganization')
    public_SYSDataImportTaskLog_: Mapped[List['PublicSYSDataImportTaskLog']] = relationship('PublicSYSDataImportTaskLog', uselist=True, foreign_keys='[PublicSYSDataImportTaskLog.SubOrganizationId]', back_populates='public_STPOrganization_')
    public_SYSDataImportErrorLog: Mapped[List['PublicSYSDataImportErrorLog']] = relationship('PublicSYSDataImportErrorLog', uselist=True, foreign_keys='[PublicSYSDataImportErrorLog.OrganizationId]', back_populates='public_STPOrganization')
    public_SYSDataImportErrorLog_: Mapped[List['PublicSYSDataImportErrorLog']] = relationship('PublicSYSDataImportErrorLog', uselist=True, foreign_keys='[PublicSYSDataImportErrorLog.SubOrganizationId]', back_populates='public_STPOrganization_')


class PublicSYSDataImportTaskLog(Base):
    __tablename__ = 'public.SYSDataImportTaskLog'
    __table_args__ = (
        ForeignKeyConstraint(['CreatedBy'], ['public.SYSUsers.UserId'], name='STPNumberSequences_fk0'),
        ForeignKeyConstraint(['ModifiedBy'], ['public.SYSUsers.UserId'], name='STPNumberSequences_fk1'),
        ForeignKeyConstraint(['OrganizationId'], ['public.STPOrganization.OrganizationId'], name='STPNumberSequences_fk2'),
        ForeignKeyConstraint(['SubOrganizationId'], ['public.STPOrganization.OrganizationId'], name='STPNumberSequences_fk3'),
        PrimaryKeyConstraint('RecId', name='DataImportTaskLog_pk'),
        UniqueConstraint('TaskId', name='public.SYSDataImportTaskLog_TaskId_key')
    )

    OrganizationId = mapped_column(Integer, nullable=False)
    RecId = mapped_column(Integer)
    TaskId = mapped_column(String(20), server_default=text("('TI-'::text || (nextval('importtask_id_seq'::regclass))::text)"))
    FileName = mapped_column(String(220))
    ImportDate = mapped_column(Date)
    FunctionalEntity = mapped_column(Enum('ExpenseRegistration', 'CashAdvance', 'Requisition', 'TravelRequisition', name='functionalentity'))
    StartDatetime = mapped_column(DateTime)
    EndDatetime = mapped_column(DateTime)
    CreatedDatetime = mapped_column(DateTime)
    CreatedBy = mapped_column(String(20))
    ModifiedDatetime = mapped_column(DateTime)
    ModifiedBy = mapped_column(String(20))
    SubOrganizationId = mapped_column(Integer)
    BulkInsertionStatus = mapped_column(Enum('Created', 'Inprogress', 'Completed', 'Error', name='bulkinsertionstatus'))
    RecordsProcessed = mapped_column(Integer)
    RecordsInserted = mapped_column(Integer)
    RecordsUpdated = mapped_column(Integer)
    RecordsFailed = mapped_column(Integer)

    public_SYSUsers: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[CreatedBy], back_populates='public_SYSDataImportTaskLog')
    public_SYSUsers_: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[ModifiedBy], back_populates='public_SYSDataImportTaskLog_')
    public_STPOrganization: Mapped['PublicSTPOrganization'] = relationship('PublicSTPOrganization', foreign_keys=[OrganizationId], back_populates='public_SYSDataImportTaskLog')
    public_STPOrganization_: Mapped[Optional['PublicSTPOrganization']] = relationship('PublicSTPOrganization', foreign_keys=[SubOrganizationId], back_populates='public_SYSDataImportTaskLog_')
    public_SYSDataImportErrorLog: Mapped[List['PublicSYSDataImportErrorLog']] = relationship('PublicSYSDataImportErrorLog', uselist=True, back_populates='public_SYSDataImportTaskLog')


class PublicSYSDataImportErrorLog(Base):
    __tablename__ = 'public.SYSDataImportErrorLog'
    __table_args__ = (
        ForeignKeyConstraint(['CreatedBy'], ['public.SYSUsers.UserId'], name='DataImportErrorLog_fk1'),
        ForeignKeyConstraint(['ModifiedBy'], ['public.SYSUsers.UserId'], name='DataImportErrorLog_fk2'),
        ForeignKeyConstraint(['OrganizationId'], ['public.STPOrganization.OrganizationId'], name='DataImportErrorLog_fk3'),
        ForeignKeyConstraint(['SubOrganizationId'], ['public.STPOrganization.OrganizationId'], name='DataImportErrorLog_fk4'),
        ForeignKeyConstraint(['TaskId'], ['public.SYSDataImportTaskLog.TaskId'], name='DataImportErrorLog_fk0'),
        PrimaryKeyConstraint('RecId', name='DataImportErrorLog_pk')
    )

    OrganizationId = mapped_column(Integer, nullable=False)
    RecId = mapped_column(Integer)
    TaskId = mapped_column(String(20))
    RowNumber = mapped_column(Integer)
    CreatedDatetime = mapped_column(DateTime)
    CreatedBy = mapped_column(String(20))
    ModifiedDatetime = mapped_column(DateTime)
    ModifiedBy = mapped_column(String(20))
    SubOrganizationId = mapped_column(Integer)
    FunctionalEntity = mapped_column(Enum('ExpenseRegistration', 'CashAdvance', 'Requisition', 'TravelRequisition', name='functionalentity'))
    FailureReason = mapped_column(Text)

    public_SYSUsers: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[CreatedBy], back_populates='public_SYSDataImportErrorLog')
    public_SYSUsers_: Mapped[Optional['PublicSYSUsers']] = relationship('PublicSYSUsers', foreign_keys=[ModifiedBy], back_populates='public_SYSDataImportErrorLog_')
    public_STPOrganization: Mapped['PublicSTPOrganization'] = relationship('PublicSTPOrganization', foreign_keys=[OrganizationId], back_populates='public_SYSDataImportErrorLog')
    public_STPOrganization_: Mapped[Optional['PublicSTPOrganization']] = relationship('PublicSTPOrganization', foreign_keys=[SubOrganizationId], back_populates='public_SYSDataImportErrorLog_')
    public_SYSDataImportTaskLog: Mapped[Optional['PublicSYSDataImportTaskLog']] = relationship('PublicSYSDataImportTaskLog', back_populates='public_SYSDataImportErrorLog')
