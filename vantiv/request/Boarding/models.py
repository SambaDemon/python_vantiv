from . .Request import Request


class CreateLegalEntity (Request):

    Address = None
    Credentials = None
    LegalEntity = None
    Principal = None
    PrincipalArray = None

    def __init__(self):
        super(CreateLegalEntity, self).__init__("boarding",
                                                "services",
                                                "createLegalEntity",
                                                "POST")


class CreateSubMerchant (Request):

    Address = None
    Credentials = None
    ECheck = None
    Merchant = None
    PrimaryContact = None
    SubMerchantFunding = None

    def __init__(self, entityID):
        super(CreateSubMerchant, self).__init__("boarding",
                                                "services",
                                                "createSubMerchant",
                                                "POST")
        self.queryParams['entityID'] = entityID


class RetrieveLegalEntity (Request):

    def __init__(self, entityID):
        super(RetrieveLegalEntity, self).__init__("boarding",
                                                  "services",
                                                  "retrieveLegalEntity",
                                                  "GET")
        self.queryParams['entityID'] = entityID


class RetrieveMccList (Request):

    def __init__(self):
        super(RetrieveMccList, self).__init__("boarding",
                                              "services",
                                              "retrieveMccList",
                                              "GET")


class RetrieveSubMerchant (Request):

    def __init__(self, entityID, subMerchantID):
        super(RetrieveSubMerchant, self).__init__("boarding",
                                                  "services",
                                                  "retrieveSubMerchant",
                                                  "GET")
        self.queryParams['entityID'] = entityID
        self.queryParams['subMerchantID'] = subMerchantID


class UpdateLegalEntity (Request):

    Address = None
    BackgroundCheckFields = None
    Credentials = None
    LegalEntity = None
    Principal = None
    PrincipalArray = None

    def __init__(self, entityID):
        super(UpdateLegalEntity, self).__init__("boarding",
                                                "services",
                                                "updateLegalEntity",
                                                "PUT")
        self.queryParams['entityID'] = entityID


class UpdateSubMerchant (Request):

    Address = None
    Credentials = None
    ECheck = None
    Merchant = None
    PrimaryContact = None
    SubMerchantFunding = None

    def __init__(self, entityID, subMerchantID):
        super(UpdateSubMerchant, self).__init__("boarding",
                                                "services",
                                                "updateSubMerchant",
                                                "PUT")
        self.queryParams['entityID'] = entityID
        self.queryParams['subMerchantID'] = subMerchantID