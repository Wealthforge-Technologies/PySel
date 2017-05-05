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
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Address"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Address Continued"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".City"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".State"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Zip Code"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Phone Number"] = "TestISS+"+str(quirk) 
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Logo Url"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Website"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Primary Color"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Secondary Color"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Legal Name"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Incorporated As"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".State of Incorporation"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Point of Contact Name"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Point of Contact Title"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Point of Contact Email Address"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Default Bank"] = "TestISS+"+str(quirk)
        self.testinfo["ISS.TestISS+" + str(quirk) + ".Employer Identification Number (EIN) / Tax ID"] = "TestISS+"+str(quirk)
