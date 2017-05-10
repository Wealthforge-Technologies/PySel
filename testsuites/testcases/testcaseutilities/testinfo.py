from random import randint

class TestInfo:

    def __init__(self):
        self.testinfo = {}

    #TODO write the json object reader to use outside data in the test cases
    def load_json(self):
        pass

    def load_defaults(self):
        quirk = randint(100000, 999999)
        self.testinfo["CCO.email"] = "oquelland@wealthforge.com"
        self.testinfo["CCO.password"] = "Test123!"
        self.testinfo["BD.WealthForge Securities.Display Name"] = "WealthForge Securities"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Display Name"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Address"] = "Test Avenue 123"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Address Continued"] = "PO 222"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".City"] = "TestCity"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".State"] = "Virginia"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Zip Code"] = "23220"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Phone Number"] = "8041234567"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Logo Url"] = "https://www.wealthforge.com/hs-fs/hubfs/WF_logo.png?t=1493926272979&width=636&name=WF_logo.png"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Website"] = "https://www.wealthforge.com"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Primary Color"] = "666666"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Secondary Color"] = "333333"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Legal Name"] = "WealthForge Legal Name"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Incorporated As"] = "LLC"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".State of Incorporation"] = "Virginia"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Point of Contact Name"] = "Test Contanct"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Point of Contact Title"] = "Test Contact Title"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Point of Contact Email Address"] = "test.emails@wealthforge.com"
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Default Bank"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Employer Identification Number (EIN) / Tax ID"] = "TestISS+"+str(quirk)
        self.testinfo["NewBDUser.First Name"] = "F" + str(randint(1,999))
        self.testinfo["NewBDUser.Last Name"] = "L" + str(randint(1,999))
        self.testinfo["NewBDUser.Full Name"] = self.testinfo["NewBDUser.First Name"] + " " + self.testinfo["NewBDUser.Last Name"]
        self.testinfo["NewBDUser.Email"] = "wealthforgedev1+"+str(quirk)+"@gmail.com"
        self.testinfo["NewBDUser.Role1"] = "Fingerprinted Person"
