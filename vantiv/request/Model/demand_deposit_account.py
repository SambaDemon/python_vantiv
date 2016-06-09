from ..schemas import Schema, fields
from ..utilities import frozen


class DemandDepositAccountSchema(Schema):
    DDAAccountType = fields.String()
    AccountNumber = fields.String()
    RoutingNumber = fields.String()
    CheckNumber = fields.String()
    CCDPaymentInformation = fields.String()


class DemandDepositAccount(object):
    __schema__ = DemandDepositAccountSchema

    DDAAccountType = None
    AccountNumber = None
    RoutingNumber = None
    CheckNumber = None
    CCDPaymentInformation = None

    __setattr__ = frozen(object.__setattr__)
