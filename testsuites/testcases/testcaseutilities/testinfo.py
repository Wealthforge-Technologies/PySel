from random import randint

class TestInfo:

    def __init__(self):
        self.testinfo = {}
        self.testissinfo = {}

    #TODO write the json object reader to use outside data in the test cases
    def load_json(self):
        pass

    def load_defaults(self):

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
        self.testinfo["IP.emailWrong"] = "mglass+z1@wealthforge.com"
        self.testinfo["IP.passwordWrong"] = "Trap1234"

        self.testinfo["txtInvestorFirstName"] = "Joe"
        self.testinfo["txtInvestorLastName"] = "Smith"
        self.testinfo["txtInvestorDOB"] = "11/16/1985"
        self.testinfo["txtInvestorSSN"] = "734-28-9123"
        self.testinfo["txtInvestorAddress1"] = "14234 Happy Lane"
        self.testinfo["txtInvestorAddress2"] = "Apt 3"
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
        self.testinfo["SpouseCRDNum"] = "3445479802"
        self.testinfo["rbSpouseFINRA"] = False

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
        self.testinfo["invAmnt"] = "2000"
        self.testinfo["ddlAccountTypes"] = "Checking"

        #Entity Registration Page
        self.testinfo["ddlEntityTypes"] = "Trust"
        self.testinfo["txtInvestorName"] = "Jeff Stephens"
        self.testinfo["txtInvestorSignatoryName"] = "Ollie Jacobs"
        self.testinfo["txtInvestorSignatoryTitle"] = "awasu"
        self.testinfo["txtInvestorEIN"] = "53-6576854"

        #Married Registration Page
        self.testinfo["txtSpouseFirstName"] = "Breanna"
        self.testinfo["txtSpouseLastName"] = "Erickson"
        self.testinfo["txtSpouseDOB"] = "05/22/1983"
        self.testinfo["txtSpouseSSN"] = "344-92-8743"
        self.testinfo["txtSpousePhone"] = "(799)169-4865"
        self.testinfo["txtSpouseEmail"] = "mglass+i5@wealthforge.com"
        self.testinfo["txtSpouseEmailConfirm"] = "mglass+i5@wealthforge.com"

        #Getting to Know You Page
        self.testinfo["address"] = "446 Ojogo Pike"
        self.testinfo["addressCont"] = "PO Box 23"
        self.testinfo["city"] = "Anderson"
        self.testinfo["stateDrop"] = "South Carolina"
        self.testinfo["zip"] = "79798"
        self.testinfo["phone"] = "(452) 312-5764"

        #Create An Account Page
        self.testinfo["fname"] = "Bryan"
        self.testinfo["lname"] = "Christensen"
        self.testinfo["email"] = "mglass+f"+str(randint(100000, 999999))+"@wealthforge.com"
        self.testinfo["confemail"] = "mglass+f"+str(randint(100000, 999999))+"@wealthforge.com"

        #Set Your New Password Page
        self.testinfo["username"] = "Test1234"
        self.testinfo["password2"] = "Test1234"

        #Investment Minimum Not Met
        self.testinfo["invAmnt"] = "200"




