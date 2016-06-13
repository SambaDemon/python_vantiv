from ..schemas import Schema, fields
from ..utilities import frozen
from ..enums import EnumField, OrderSourceEnum, TaxTypeEnum


class TransactionSchema(Schema):
    CustomerID = fields.String()
    PartialCapture = fields.String()
    ReferenceNumber = fields.String()
    AuthorizationDate = fields.Date()
    ApprovalNumber = fields.String()
    TransactionAmount = fields.String()
    TransactionID = fields.String()
    ConvenienceFeeAmount = fields.Decimal()
    PartialApprovedFlag = fields.Bool()
    FraudFilterOverride = fields.Bool()
    SurchargeFee = fields.String()
    ActionReason = fields.String()
    Verify = fields.String()
    TransactionType = fields.String()
    OrderSource = EnumField(OrderSourceEnum, by_value=True)
    TaxType = EnumField(TaxTypeEnum, by_value=True)


class Transaction(object):
    __schema__ = TransactionSchema

    CustomerID = None
    PartialCapture = None
    ReferenceNumber = None
    AuthorizationDate = None
    ApprovalNumber = None
    TransactionAmount = None
    TransactionID = None
    ConvenienceFeeAmount = None
    PartialApprovedFlag = None
    FraudFilterOverride = None
    SurchargeFee = None
    ActionReason = None
    Verify = None
    TransactionType = None
    OrderSource = None
    TaxType = None

    __setattr__ = frozen(object.__setattr__)