from enum import Enum,IntEnum as SourceIntEnum
from typing import Type

class _EnumBase:
    @classmethod
    def get_member_keys(cls: Type[Enum]) -> list[str]:
        return [name for name in cls.__members__.keys()]

    @classmethod
    def get_member_values(cls: Type[Enum]) -> list:
        return [item.value for item in cls.__members__.values()]
    
class IntEnum(_EnumBase, SourceIntEnum):
    """Integer Enum"""

    pass


class StrEnum(_EnumBase, str, Enum):
    """String Enum"""

    pass

class FieldType(StrEnum):
    """Field Type"""

    Email = 'Email'
    Date = 'Date'
    Amount = 'Amount'
    Integer = 'Integer'
    Decimal = 'Decimal'
    List = 'List'
    Url = 'Url'
    Text = 'Text'
    DateTime = 'Date&Time'
    Percent = 'Percent'
    Checkbox = 'Checkbox'
    LongInteger = 'Long Integer'

class ObjectName(StrEnum):
    """Object Name"""

    ExpenseCategories = 'EXPExpenseCategories'
    Employee = 'EMPEmployee'
    ExpenseHeader = 'EXPExpenseHeader'
    ExpenseTrans = 'EXPExpenseTrans'

class AddressPurpose(StrEnum):
    """Address Purpose"""

    Permanent = 'Permanent'
    Contact = 'Contact'
    Business = 'Business'

class ApplyTaxOn(StrEnum):
    """Apply TaxOn"""

    BasePrice = 'Base Price'
    Discounted = 'Discounted'
    Price = 'Price'

class Area(StrEnum):
    """Area"""

    ExpenseRequisition = 'Expense Requisition'
    TravelRequisition = 'Travel Requisition'
    CashAdvanceRequisition = 'Cash Advance Requisition'

class CategoryType(StrEnum):
    """Category Type"""

    Created = 'Created'
    Approved = 'Approved'
    Rejected = 'Rejected'
    Cancelled = 'Cancelled'
    Escalated = 'Escalated'

class CompletionPolicy(StrEnum):
    """Completion Policy"""

    SingleApprover = 'SingleApprover'
    AllApprovers = 'AllApprovers'
    MajorityOfApprovers = 'MajorityOfApprovers'

class ConditionType(StrEnum):
    """Condition Type"""

    AlwaysExecute = 'AlwaysExecute'
    ConditionalBased = 'ConditionalBased'

class DayInMonth(StrEnum):
    """Day In Month"""

    FirstDay = 'First Day'
    LastDay = 'Last Day'
    Second = '2nd'
    Third = '3rd'
    Fourth = '4th'
    Fifth = '5th'
    Sixth = '6th'
    Seventh = '7th'
    Eighth = '8th'
    Ninth = '9th'
    Tenth = '10th'
    Eleventh = '11th'
    Twelfth = '12th'
    Thirteenth = '13th'
    Fourteenth = '14th'
    Fifteenth = '15th'
    Sixteenth = '16th'
    Seventeenth = '17th'
    Eighteenth = '18th'
    Nineteenth = '19th'
    Twentieth = '20th'
    TwentyFirst = '21st'
    TwentySecond = '22nd'
    TwentyThird = '23rd'
    TwentyFourth = '24th'
    TwentyFifth = '25th'
    TwentySixth = '26th'
    TwentySeventh = '27th'
    TwentyEighth = '28th'
    TwentyNinth = '29th'
    Thirtieth = '30th'
    NoneValue = 'None'

class DecimalPlace(StrEnum):
    """Decimal Place"""

    Zero = '0'
    One = '1'
    Two = '2'
    Three = '3'
    Four = '4'
    Five = '5'
    Six = '6'

class DecimalSeparator(StrEnum):
    """Decimal Separator"""

    Dot = '.'
    Comma = ','

class DefaultDateFormat(StrEnum):
    """Default Date Format"""

    YYYY_MM_DD = 'YYYY/MM/DD'
    MM_dd_yyyy = 'MM-dd-yyyy'
    YYYYMMDD = 'YYYY-MM-DD'
    MMddyyyy = 'MM.dd.yyyy'
    dd_MM_yyyy = 'dd.MM.yyyy'
    YYYYMM_DD = 'YYYY.MM.DD'
    d_MMMM_yyyy = 'd MMMM yyyy'

class DimensionType(StrEnum):
    """DimensionType"""

    System = 'System'
    Custom = 'Custom'

class EmploymentStatus(StrEnum):
    """Employment Status"""

    Active = 'Active'
    Inactive = 'Inactive'
    OnLongVacation = 'On Long Vacation'

class FieldName(StrEnum):
    """Field Name"""

    Merchant = 'Merchant'
    Category = 'Category'
    Project = 'Project'
    PaidWith = 'Paid With'
    Comment = 'Comment'
    Country = 'Country'
    VatAmount = 'Vat Amount'
    VatPercentage = 'Vat Percentage'

class FunctionalEntity(StrEnum):
    """Functional Entity"""

    ExpenseRegistration = 'ExpenseRegistration'
    CashAdvance = 'CashAdvance'
    Requisition = 'Requisition'
    TravelRequisition = 'TravelRequisition'

class Gender(StrEnum):
    """Gender"""

    Male = 'Male'
    Female = 'Female'
    NonSpecific = 'Non-Specific'

class GlobalFiscalYearId(StrEnum):
    """Global Fiscal Year Id"""

    JAN_DEC = 'JAN-DEC'
    FEB_JAN = 'FEB-JAN'
    MAR_FEB = 'MAR-FEB'
    APR_MAR = 'APR-MAR'
    MAY_APR = 'MAY-APR'
    APR_MAY = 'APR-MAY'
    MAY_JUN = 'MAY-JUN'
    JUN_JUL = 'JUN-JUL'
    JUL_AUG = 'JUL-AUG'
    AUG_SEP = 'AUG-SEP'
    SEP_OCT = 'SEP-OCT'
    OCT_NOV = 'OCT-NOV'
    NOV_DEC = 'NOV-DEC'
    DEC_JAN = 'DEC-JAN'

class HolidayType(StrEnum):
    """Holiday Type"""

    NationalHolidays = 'National Holidays'
    ReligiousHolidays = 'Religious Holidays'
    SecularHolidays = 'Secular Holidays'
    StatutoryHolidays = 'Statutory Holidays'
    CivicHolidays = 'Civic Holidays'

class Industries(StrEnum):
    """Industries"""

    Agriculture = 'Agriculture'
    MetalProduction = 'Metal Production'
    ChemicalIndustry = 'Chemical Industry'
    Construction = 'Construction'
    Education = 'Education'
    FinancialServices = 'Financial Services'
    ProfessionalServices = 'Professional Services'
    FoodIndustry = 'Food Industry'
    HealthCareIndustry = 'HealthCare Industry'
    PublicServices = 'Public Services'
    Mining = 'Mining'
    MechanicalAndElectrical = 'Mechanical And Electrical'
    Medical = 'Medical'
    OilAndGasIndustry = 'Oil And Gas Industry'
    PostalAndTelecom = 'Postal And Telecom'
    ShippingTransportation = 'Shipping/Transportation'
    TextilesClothing = 'Textiles/Clothing'
    Utilities = 'Utilities'

class LedgerAccountType(StrEnum):
    """Ledger Account Type"""

    CurrentAssets = 'Current Assets'
    NonCurrentAssets = 'Non-Current Assets'
    CurrentLiabilities = 'Current Liabilities'
    NonCurrentLiabilities = 'Non-Current Liabilities'
    OwnersEquity = "Owners Equity"
    DrawingsOrDividends = 'Drawings or Dividends'
    RevenueAccounts = 'Revenue Accounts'
    IncomeAccounts = 'Income Accounts'
    ExpenseAccounts = 'Expense Accounts'
    ContraAccounts = 'Contra Accounts'
    SuspenseAccounts = 'Suspense Accounts'
    NominalAccounts = 'Nominal Accounts'
    TemporaryAccounts = 'Temporary Accounts'

class LoginType(StrEnum):
    """Login Type"""

    System = 'System'
    User = 'User'

class MaritalStatus(StrEnum):
    """Marital Status"""

    Married = 'Married'
    Single = 'Single'
    Widowed = 'Widowed'
    Divorced = 'Divorced'
    Cohabiting = 'Cohabiting'
    RegisteredPartnership = 'Registered Partnership'
    Concubine = 'Concubine'
    Separated = 'Separated'

class OrganizationType(StrEnum):
    """Organization Type"""

    Business = 'Business'
    Individual = 'Individual'

class PaidBy(StrEnum):
    """Paid By"""

    Employee = 'Employee'
    Customer = 'Customer'
    Organization = 'Organization'

class ParticipantType(StrEnum):
    """Participant Type"""

    RoleBased = 'RoleBased'
    UserBased = 'UserBased'

class PolicyAction(StrEnum):
    """Policy Action"""

    AutoApproveExpenseRegistration = 'Auto Approve Expense Registration'
    AutoRejectExpenseRegistration = 'Auto Reject Expense Registration'
    DoNotAllowUserToSubmitOrApproveExpense = 'Do Not Allow User To Submit Or Approve Expense'
    AllowUsersToSubmitAndApproveWithWarning = 'Allow Users To Submit And Approve But Display Warning Message'
    DoNotAllowUserToSubmitWithJustification = 'Do Not Allow User To Submit Until They Enter Justification'

class ProviderType(StrEnum):
    """Provider Type"""

    Manual = 'Manual'
    OpenExchangeAPI = 'Open Exchange API'
    Banks = 'Banks'

class Remainder(StrEnum):
    """Remainder"""

    ExpenseReportSubmission = 'Expense Report Submission'
    BudgetStatusUpdates = 'Budget Status Updates'
    PendingReimbursements = 'Pending Reimbursements'
    UnapprovedRequests = 'Unapproved Requests'
    OverdueApproval = 'Overdue Approval'
    UnreportedExpense = 'Unreported Expense'

class ReminderType(StrEnum):
    """Reminder Type"""

    Weekly = 'Weekly'
    Monthly = 'Monthly'

class RoundingMethod(StrEnum):
    """Rounding Method"""

    Normal = 'Normal'
    Upward = 'Upward'
    Downward = 'Downward'

class SLADurationUnit(StrEnum):
    """SLA DurationUnit"""
    
    Days = 'Days'
    Weeks = 'Weeks'
    Months = 'Months'

class Status(StrEnum):
    """Status"""

    Created = 'Created'
    SentInvitation = 'Sent Invitation'
    ResentInvitation = 'Resent Invitation'
    Registered = 'Registered'
    PasswordReset = 'Password Reset'

class StorageType(StrEnum):
    """Storage Type"""

    DataBase = 'DataBase'
    LocalStorage = 'Local Storage'
    AWSStorage = 'AWS storage'
    AzureBlob = 'Azure Blob'

class TaxCalculationMethod(StrEnum):
    """Tax Calculation Method"""

    Simple = 'Simple'
    Compound = 'Compound'
    Surcharge = 'Surcharge'

class ThemeMenuType(StrEnum):
    """Theme Menu Type"""

    HorizontalLayout = 'Horizontal Layout'
    VerticalLayout = 'Vertical Layout'

class TourStatus(StrEnum):
    """Tour Status"""

    Active = 'Active'
    Completed = 'Completed'
    Requested = 'Requested'

class TrackingContext(StrEnum):
    """Tracking Context"""

    ExpenseRequisition = 'Expense Requisition'
    CashAdvanceRequisition = 'Cash Advance Requisition'
    TravelRequisition = 'Travel Requisition'

class UseValuesFrom(StrEnum):
    """Use Values From"""

    Departments = 'Departments'
    Branches = 'Branches'
    Projects = 'Projects'
    Employees = 'Employees'
    ExpenseCategories = 'ExpenseCategories'
    Vendors = 'Vendors'

class Weekday(StrEnum):
    """Weekday"""

    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Friday = 'Friday'
    Saturday = 'Saturday'
    Sunday = 'Sunday'
    none = 'None'

class WorkflowStatus(StrEnum):
    """Workflow Status"""

    Created = 'Created'
    Approved = 'Approved'
    Rejected = 'Rejected'
    Cancelled = 'Cancelled'
    Escalated = 'Escalated'

class WorkflowTrackingStatus(StrEnum):
    """Workflow Tracking Status"""

    Created = 'Created'
    InReview = 'In Review'
    Approved = 'Approved'
    Rejected = 'Rejected'
    Completed = 'Completed'