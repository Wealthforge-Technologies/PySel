from random import randint

class TestInfo:

    def __init__(self):
        self.testinfo = {}
        self.testissinfo = {}
        self.testbankinfo = {}
        self.testOfferInfo = {}

        self.testTermInfoDefaults = {}
        self.testTermInfoOther = {}

    #TODO write the json object reader to use outside data in the test cases
    def load_json(self):
        pass

    def load_defaults(self):

        self.testOfferInfo["offeringTitle"] = "Test Offer+"+str(randint(100000, 999999))
        self.testOfferInfo["regTypeDropdown"] = "RegC"
        self.testOfferInfo["dateStart"] = ""  # this is not dynamic, it will always select the year before
        self.testOfferInfo["dateEnd"] = ""  # this is not dynamic, it will always select the year after
        self.testOfferInfo["minOfferRaise"] = "2,000,000"
        self.testOfferInfo["maxOfferRaise"] = "5,000,000"

        self.testTermInfoDefaults["termType"] = "Debenture"
        self.testTermInfoDefaults["classTitle"] = "Class Title 123"
        self.testTermInfoDefaults["minInvestment"] = "100.33"
        self.testTermInfoDefaults["minTermRaise"] = "1,000,000"
        self.testTermInfoDefaults["maxTermRaise"] = "4,000,000"
        self.testTermInfoDefaults["price"] = "24.35"
        self.testTermInfoDefaults["notesIssued"] = "4567"
        self.testTermInfoDefaults["paymentTypes"] = 0b11110


        self.testTermInfoOther["interestRate"] = "7.65"
        self.testTermInfoOther["maturityMonths"] = "45"
        self.testTermInfoOther["paymentFreqDropdown"] = "Monthly" # Dropdown Options: Monthly, Quarterly, Semi-annually, Annually, Cumulative
        self.testTermInfoOther["conversionRatio"] = "3.45"

        self.testissinfo["displayNameInput"] = "TestISS+"+str(randint(100000, 999999))
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

        self.testbankinfo["inputBankName"] = "PySel Bank"+str(randint(100000, 999999))
        self.testbankinfo["inputDestinationRoutingNum"] = ""+str(randint(0, 999999999)).zfill(9) # must be 9 digits
        self.testbankinfo["inputOriginName"] = "PySel Origin Name"
        self.testbankinfo["inputOriginRoutingNum"] = ""+str(randint(0, 999999999)).zfill(9)  # must be 9 digits
        self.testbankinfo["inputCompany"] = ""+str(randint(0, 9))
        self.testbankinfo["inputClass"] = "WEB"  # Dropdown
        self.testbankinfo["inputAddress"] = "343 PySel Ave."
        self.testbankinfo["inputAddressCont"] = "Apt. 2071"
        self.testbankinfo["inputCity"] = "Selenium City"
        self.testbankinfo["inputState"] = "Kentucky"  # Dropdown
        self.testbankinfo["inputZip"] = "15625"
        self.testbankinfo["inputPhone"] = "(154) 480-4416"

        # self.testinfo["environment"] = "qa1.wealthforge.org"
        self.testinfo["CCO.email"] = "oquelland@wealthforge.com"
        self.testinfo["CCO.password"] = "Test123!"
        self.testinfo["BD.WealthForge Securities.Display Name"] = "WealthForge Securities"


        self.testinfo["testissinfo"] = self.testissinfo

        self.testinfo["NewBDUser.First Name"] = "F" + str(randint(1,999))
        self.testinfo["NewBDUser.Last Name"] = "L" + str(randint(1,999))
        self.testinfo["NewBDUser.Full Name"] = self.testinfo["NewBDUser.First Name"] + " " + self.testinfo["NewBDUser.Last Name"]
        self.testinfo["NewBDUser.Email"] = "wealthforgedev1+"+str(randint(100000, 999999))+"@gmail.com"
        self.testinfo["NewBDUser.Role1"] = "Fingerprinted Person"
        self.testinfo["NewBDUser.Password"] = "Test123!"

        self.testinfo["IP.email"] = "jgoldhamer+i4@wealthforge.com"
        self.testinfo["IP.password"] = "Testing123!"

        self.testinfo["txtInvestorFirstName"] = "Joe"
        self.testinfo["txtInvestorLastName"] = "Smith"
        self.testinfo["txtInvestorDOB"] = "11/16/1985"
        self.testinfo["txtInvestorSSN"] = "734-28-9123"
        self.testinfo["txtInvestorAddress1"] = "14234 Happy Lane"
        self.testinfo["txttxtInvestorAddress2"] = "Apt 3"
        self.testinfo["txtInvestorCity"] = "Plano"
        self.testinfo["ddlInvestorStateProvs"] = "Texas"
        self.testinfo["txtInvestorPostalCode"] = "43234"
        self.testinfo["txtInvestorPhone"] = "(864) 234-0945"
        self.testinfo["txtInvestorEmail"] = "mglass+i@wealthforge.com"

        # Employment Status Page
        self.testinfo["Employment Status"] = "Currently Employed"
        self.testinfo["otherOpport"] = True
        self.testinfo["rbFINRA"] = True
        self.testinfo["CRD Number"] = "344545667"

        # Suitability Page
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
        self.testinfo["invAmnt"] = str(randint(100,999999))
        self.testinfo["ddlAccountTypes"] = "Checking"



