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

        self.testinfo["IP.email"] = "jgoldhamer+i@wealthforge.com"
        self.testinfo["IP.password"] = "Testing123!"

        self.testinfo["txtInvestorFirstName"] = "Joe"
        self.testinfo["txtInvestorLastName"] = "Smith"
        self.testinfo["txtInvestorDOB"] = "11161985"
        self.testinfo["txtInvestorSSN"] = "734289123"
        self.testinfo["txtInvestorAddress1"] = "14234 Happy Lane"
        self.testinfo["txttxtInvestorAddress2"] = "Apt 3"
        self.testinfo["txtInvestorCity"] = "Plano"
        self.testinfo["ddlInvestorStateProvs"] = "Texas"
        self.testinfo["txtInvestorPostalCode"] = "43234"
        self.testinfo["txtInvestorPhone"] = "8642340945"
        self.testinfo["txtInvestorEmail"] = "mglass+i@wealthforge.com"

        self.testinfo["ddlInvestorEmploymentStatus"] = "Currently Employed"

        self.testinfo["sq-10"] = "Capital Preservation – you seek to preserve capital and are willing to accept a lower rate of return in exchange."
        self.testinfo["sq-20"] = "Less than 2 years"
        self.testinfo["sq-30"] = "Conservative"
        self.testinfo["sq-40"] = "Less than 2 years"
        self.testinfo["sq-50"] = "None"
        self.testinfo["sq-60"] = "Less than $250,000 USD"
        self.testinfo["sq-70"] = "Greater than $250,000 USD"
        self.testinfo["sq-80"] = "Greater than $250,000 USD"
        self.testinfo["sq-90"] = "Greater than $500,000"
        self.testinfo["sq-100"] = "Greater than $100,000"
        self.testinfo["sq-110"] = "Less than 20%"
        self.testinfo["sq-120"] = "Yes"
        self.testinfo["sq-130"] = "Yes"
        self.testinfo["invAmnt"] = "2000"

        self.testinfo["ddlAccountTypes"] = "Checking"
        self.testinfo["ACHAcctName"] = "Joe Smith"
        self.testinfo["ACHRoutNum"] = "449398156"
        self.testinfo["ACHRoutNumConf"] = "449398156"
        self.testinfo["ACHAcctNum"] = "4471325151914572"
        self.testinfo["ACHAcctNumConf"] = "4471325151914572"

        self.testinfo["ddlEntityTypes"] = "Trust"
        self.testinfo["txtInvestorName"] = "Jeff Stephens"
        self.testinfo["txtInvestorSignatoryName"] = "Ollie Jacobs"]
        self.testinfo["txtInvestorSignatoryTitle"] = "awasu"
        self.testinfo["txtInvestorEIN"] = "53-6576854"

        self.testinfo["txtSpouseFirstName"] = "Breanna"
        self.testinfo["txtSpouseLastName"] = "Erickson"
        self.testinfo["txtSpouseDOB"] = "05/22/1983"
        self.testinfo["txtSpouseSSN"] = "344-92-8743"
        self.testinfo["txtSpousePhone"] = "(799)169-4865"
        self.testinfo["txtSpouseEmail"] = "mglass+i5@wealthforge.com"
        self.testinfo["txtSpouseEmailConfirm"] = "mglass+i5@wealthforge.com"




