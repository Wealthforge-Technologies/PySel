from random import randint

class TestInfo:

    def __init__(self):
        self.testinfo = {}
        self.testissinfo = {}

    #TODO write the json object reader to use outside data in the test cases
    def load_json(self):
        pass

    def load_defaults(self):
        quirk = randint(100000, 999999)
        self.testinfo["environment"] = "qa1.wealthforge.org"
        self.testinfo["CCO.email"] = "oquelland@wealthforge.com"
        self.testinfo["CCO.password"] = "Test123!"
        self.testinfo["BD.WealthForge Securities.Display Name"] = "WealthForge Securities"

        self.testissinfo["displayNameInput"] = "TestISS+"+str(quirk)
        self.testissinfo["address1Input"] = "Test Avenue 123"
        self.testissinfo["address2Input"] = "PO 222"
        self.testissinfo["cityInput"] = "TestCity"
        self.testissinfo["stateDrop"] = "Virginia"
        self.testissinfo["zipInput"] = "23220"
        self.testissinfo["phoneInput"] = "(804) 123-4567"
        self.testissinfo["logoUrlInput"] = "https://www.wealthforge.com/hs-fs/hubfs/WF_logo.png?t=1493926272979&width=636&name=WF_logo.png"
        self.testissinfo["urlInput"] = "https://www.wealthforge.com"
        self.testissinfo["colorPrimaryInput"] = "666666"
        self.testissinfo["colorSecondaryInput"] = "333333"
        self.testissinfo["legalInput"] = "WealthForge Legal Name"
        self.testissinfo["corpTypeSelect"] = "LLC"
        self.testissinfo["incorpStateDrop"] = "Virginia"
        self.testissinfo["pocInput"] = "Test Contact"
        self.testissinfo["poctInput"] = "Test Contact Title"
        self.testissinfo["pocEmailInput"] = "wealthforgedev1@gmail.com"
        self.testissinfo["issBankSelect"] = "Atlantic Capital Bank"
        self.testissinfo["taxInput"] = "12-3456789"

        self.testinfo["testissinfo"] = self.testissinfo

        self.testinfo["NewBDUser.First Name"] = "F" + str(randint(1,999))
        self.testinfo["NewBDUser.Last Name"] = "L" + str(randint(1,999))
        self.testinfo["NewBDUser.Full Name"] = self.testinfo["NewBDUser.First Name"] + " " + self.testinfo["NewBDUser.Last Name"]
        self.testinfo["NewBDUser.Email"] = "wealthforgedev1+"+str(quirk)+"@gmail.com"
        self.testinfo["NewBDUser.Role1"] = "Fingerprinted Person"
        self.testinfo["NewBDUser.Password"] = "Test123!"
