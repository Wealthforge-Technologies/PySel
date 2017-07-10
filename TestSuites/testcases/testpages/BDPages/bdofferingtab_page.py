from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage


class BDOfferingTabPage(BasePage):
    search = PageElement(id_='search')
    hamburger = PageElement(id_='appDrawerToggle')
    dots = PageElement(css='#bs-example-navbar-collapse-1 > ul > li > a')

    def __init__(self):
        BasePage.__init__(self,
                          url='/BD/#/rad',
                          title='WF: Broker Dealer')
        self.treespace = {}


    #This function populates the treespace variable.
    #The treespace variable is a dictionary where the keys are the display names of the 'nodes' in
    #the tree on the left on the offering tab and the values are lists
    #The lists look like: (node_div, dots_anchor_element, (dots_option_1, dots_option_2, ...))
    #So the list actually contains an inner list for each option under the dots dropdown menu
    #If you wanted to touch dots_option_2 you would do:
    #treespace["node_display_name"][2][1].click()
    def load_treenodes(self):
        self.treespace = {}
        assert self.driver.find_elements_by_xpath("//*[contains(@href,'#/bd-diligence')]") is not None
        orgs = self.driver.find_elements_by_xpath("//*[contains(@href,'#/bd-diligence')]")
        print(orgs)
        orgsoptions = []
        for org in orgs:
            idstring = str(org.get_attribute("href")).split("?parent=")[1]
            containsidstring = "//a[contains(@href,'" + idstring + "')]"
            assert self.driver.find_elements_by_xpath(containsidstring) is not None
            orgsoptions.append(self.driver.find_elements_by_xpath(containsidstring))
        assert self.driver.find_elements_by_xpath("//div[contains(@href,'#/bd-diligence/create?parent=')]/../../a") is not None
        orgsdots = self.driver.find_elements_by_xpath("//div[contains(@href,'#/bd-diligence/create?parent=')]/../../a")
        assert len(orgs) == len(orgsdots) == len(orgsoptions)
        for treenode in zip(orgs, orgsdots, orgsoptions):
            self.treespace[treenode[0].get_attribute("textContent").lstrip().split('\n')[1].lstrip()] = treenode
        assert self.driver.find_elements_by_xpath("//div[contains(@href,'#/bd-diligence/create?parent=')]") is not None
        users = self.driver.find_elements_by_xpath("//div[contains(@href,'#/bd-diligence/create?parent=')]")
        for user in users:
            self.treespace[user.get_attribute("textContent").lstrip().split('\n')[0]] = user
        print(self.treespace)

    def get_treenode(self, displayNameInput):
        print(displayNameInput)
        print(self.treespace)
        waitForAngular(self.driver)
        elem = self.treespace[displayNameInput[0]][0]
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        return elem
