from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
import re
import time
from testutilities import Settings as S

class BDOfferingTabPage(BasePage):
    search = PageElement(id_='search')
    hamburger = PageElement(id_='appDrawerToggle')
    dots = PageElement(css='#bs-example-navbar-collapse-1 > ul > li > a')

    def __init__(self):
        BasePage.__init__(self,
                          url='/BD/#/rad',
                          title='WF: Broker Dealer')
        self.orgTree = {}
        self.offTree = {}


    #This function populates the treespace variable.
    #The treespace variable is a dictionary where the keys are the display names of the 'nodes' in
    #the tree on the left on the offering tab and the values are lists
    #The lists look like: (node_div, dots_anchor_element, (dots_option_1, dots_option_2, ...))
    #So the list actually contains an inner list for each option under the dots dropdown menu
    #If you wanted to touch dots_option_2 you would do:
    #treespace["node_display_name"][2][1].click()
    def load_treenodes(self):
        orgs = self.driver.find_elements_by_css_selector("div[ui-sref=\"diligence({parent: org.id, parentType: org.org_type})\"]")
        if S.VERBOSITY >=5: print('orgs #: ', orgs.__len__())
        startTime = time.time()

        for org in orgs:
            # Gets the name of the org. The text includes the number next to the card that has the number of orgs and
            # offerings in it so we have to regex it out

            orgName = self.driver.execute_script("return document.evaluate('child::text()[3]', arguments[0], null, XPathResult.STRING_TYPE, null).stringValue", org).strip()
            orgId = str(org.find_element_by_xpath('parent::*/parent::*/parent::*').get_attribute("ng-id")).split("accordion")[1]
            dots = org.find_element_by_xpath('parent::*/following-sibling::*[1]')
            orgOptions = self.driver.find_elements_by_css_selector('[href="#/bd-diligence/create?parent=' + orgId + '"]')
            self.orgTree[orgId] = {'orgElem': org,
                                   'orgName': orgName,
                                   'dots': dots,
                                   'orgOptions': orgOptions}

        offerings = self.driver.find_elements_by_css_selector("div[ui-sref=\"diligence.editOffering({parent:org.issuer,id:org.id})\"]")
        if S.VERBOSITY >= 5: print('offer #: ', offerings.__len__())

        for off in offerings:
            # WHEW this was a doozy.  apparently text() operates as an array and every node under an element has it, but
            #  it is usually whitespace.  Found this out from https://stackoverflow.com/a/11744783/5454556
            offeringName = self.driver.execute_script("return document.evaluate('child::text()[3]', arguments[0], null, XPathResult.STRING_TYPE, null).stringValue", off).strip()
            if S.VERBOSITY >= 10: print('Offering Name: ', offeringName)

            # Offering Status from Tree
            offeringStatus = self.driver.execute_script("return document.evaluate('child::span', arguments[0], null, XPathResult.STRING_TYPE, null).stringValue", off)
            if S.VERBOSITY >= 10: print('Offering Status: ', offeringName)

            dots = off.find_element_by_xpath('parent::*/following-sibling::*[1]')

            offId = str(off.get_attribute("href")).split("id=")[1]

            offOptions = self.driver.find_elements_by_css_selector('[href="#/bd-diligence/diligence?id=' + offId + '"]')

            self.offTree[offId] = {'offeringElem': off,
                                   'offeringName': offeringName,
                                   'dots': dots,
                                   'offOptions : ': offOptions
                                   }

        if S.VERBOSITY >= 5: print('Offering Tree loaded in ', time.time()-startTime, ' seconds')


    #ORG FUNCTIONS

    def getOrgIdByName(self, name):
        """
        Returns the ID from the (hopefully) unique Org Name.
        *NOTE: Returns the first result of a name if there is more than one!
        The clicking functions on this page use the ID since those are unique.
        :param name: name of the Org
        :return: ID
        """
        result = None
        for org in self.orgTree.items():
            if org[1]['orgName'] == name:
                result = org[0]

        assert result is not None, 'ERROR: ORG NOT FOUND IN OFFERING TREE: ' + name
        return result

    def clickCreateOfferingByOrgId(self, id):
        # clicks context menu and then clicks the Create Offering option
        self.orgTree[id]['dots'].click()
        waitForAngular(self.driver)

        self.orgTree[id]['orgOptions'][0].click() #only one option right now
        waitForAngular(self.driver)


    # OFFERING FUNCTIONS

    def getOfferIdByName(self, name):
        """
        Returns the ID from the (hopefully) unique Offering Name.
        *NOTE: Returns the first result of a name if there is more than one!
        The clicking functions on this page use the ID since those are unique.
        :param name: name of the offering
        :return: ID
        """
        result = None
        for off in self.offTree.items():
            if off[1]['orgName'] == name:
                result = off[0]

        assert result is not None, 'ERROR: OFFERING NOT FOUND IN OFFERING TREE: ' + name
        return result

    def clickOfferingWorkflowByOffId(self, id):
        # clicks context menu and then clicks the Offering Workflow option
        self.offTree[id]['dots'].click()
        waitForAngular(self.driver)
        self.offTree[id]['offOptions'][0].click() #only one option right now
        waitForAngular(self.driver)


    def clickOfferingByOffId(self, id):
        self.offTree[id]['offeringElem'].click()
        waitForAngular(self.driver)

