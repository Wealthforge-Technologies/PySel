from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage

class IPGetStarted(BasePage):
    btnStart = PageElement(id_='btnStart')
    btnResume = PageElement(id_='btnResume')
    btnStartOver = PageElement(xpath='//*[@id="resumeProgress"]/div[2]/button')

    #TODO: temporary start new investment button
    #btnStart = PageElement(xpath='//*[@id="resumeProgress"]/div[2]/button')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/ready',
                          title='WF: Investor Platform')

    def clickGetStarted(self):
        self.btnStart.click()
        waitForAngular(self.driver)


    def clickResume(self):
        self.btnResume.click()
        waitForAngular(self.driver)


    def clickStartOver(self):
        self.btnStartOver.click()
        waitForAngular(self.driver)
