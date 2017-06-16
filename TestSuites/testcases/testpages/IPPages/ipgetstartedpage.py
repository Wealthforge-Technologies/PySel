from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage

class IPGetStarted(BasePage):
    # btnStart = PageElement(xpath='//*[@id="resumeProgress"]/div[2]/button')
    # btnStart = PageElement(id_='btnStart')
    #TODO: Resume investments

    #TODO: temporary start new investment button
    btnStart = PageElement(xpath='//*[@id="resumeProgress"]/div[2]/button')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/ready',
                          title='WF: Investor Platform')

    def clickGetStarted(self):

        self.btnStart.click()
        waitForAngular(self.driver)
