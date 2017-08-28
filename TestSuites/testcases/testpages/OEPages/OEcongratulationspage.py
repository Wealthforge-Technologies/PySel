from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage


class OECongratulationsPage(BasePage):
    btnStartNew = PageElement(xpath='/html/body/app-root/md-sidenav-container/div[4]/div/div/ng-component/div/div[2]/md-card/md-card-actions/button/span')


    def __init__(self):
        BasePage.__init__(self,
                          url='https://ci-order-entry.wealthforge.org/congratulations',
                          title='Order Entry')

    def clickStartNewOE(self):
        self.btnStartNew.click()
        waitForAngular(self.driver)