from ..schemas import Schema, fields
from ..utilities import frozen


class ApplicationSchema(Schema):
    ApplicationID = fields.String()


class Application(object):
    __schema__ = ApplicationSchema

    ApplicationID = None

    __setattr__ = frozen(object.__setattr__)
