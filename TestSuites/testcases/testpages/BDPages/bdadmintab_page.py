from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage


class BDAdminTabPage(BasePage):
    search = PageElement(id_='search')
    hamburger = PageElement(id_='appDrawerToggle')
    dots = PageElement(css='#bs-example-navbar-collapse-1 > ul > li > a')
    menuDashboardAdmin = PageElement(id_='menuDashboardAdmin')

    def __init__(self):
        BasePage.__init__(self,
                          url='/BD/#/rad',
                          title='WF: Broker Dealer')
        self.treespace = {}

    #TEMPORARY since BDHomePage is acting weird and opening a new window
    def clickAdmin(self):

        # self.hamburger.click()
        waitForAngular(self.driver)
        self.menuDashboardAdmin.click()
        waitForAngular(self.driver)

    #This function populates the treespace variable.
    #The treespace variable is a dictionary where the keys are the display names of the 'nodes' in
    #the tree on the left on the admin tab and the values are lists
    #The lists look like: (node_div, dots_anchor_element, (dots_option_1, dots_option_2, ...))
    #So the list actually contains an inner list for each option under the dots dropdown menu
    #If you wanted to touch dots_option_2 you would do:
    #treespace["node_display_name"][2][1].click()
    def load_treenodes(self):
        self.treespace = {}
        assert self.driver.find_elements_by_xpath("//*[contains(@href,'#/rad/editOrg?id=')]") is not None
        orgs = self.driver.find_elements_by_xpath("//*[contains(@href,'#/rad/editOrg?id=')]")
        orgsoptions = []
        for org in orgs:
            idstring = str(org.get_attribute("href")).split("?id=")[1]
            containsidstring = "//a[contains(@href,'" + idstring + "')]"
            assert self.driver.find_elements_by_xpath(containsidstring) is not None
            orgsoptions.append(self.driver.find_elements_by_xpath(containsidstring))
        assert self.driver.find_elements_by_xpath("//div[contains(@href,'#/rad/editOrg?id=')]/../../a") is not None
        orgsdots = self.driver.find_elements_by_xpath("//div[contains(@href,'#/rad/editOrg?id=')]/../../a")
        assert len(orgs) == len(orgsdots) == len(orgsoptions)
        for treenode in zip(orgs, orgsdots, orgsoptions):
            self.treespace[treenode[0].get_attribute("textContent").lstrip().split('\n')[1].lstrip()] = treenode
        assert self.driver.find_elements_by_xpath("//div[contains(@href,'#/rad/editUser?id=')]") is not None
        users = self.driver.find_elements_by_xpath("//div[contains(@href,'#/rad/editUser?id=')]")
        for user in users:
            self.treespace[user.get_attribute("textContent").lstrip().split('\n')[0]] = user

    def get_treenode(self, displayNameInput):
        print(displayNameInput)
        print(self.treespace)
        waitForAngular(self.driver)
        elem = self.treespace[displayNameInput[0]][0]
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        return elem
