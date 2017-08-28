from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage


class OEChooseAccountPage(BasePage):
    btnPickAcct = PageElement(xpath='//*[@id="view_container"]/form/div[2]/div/div/div/ul/li[2]/div/div[1]/img')


    def __init__(self):
        BasePage.__init__(self,
                          url='https://accounts.google.com/signin/oauth/oauthchooseaccount?client_id=104565000066-q7q63bouq2ct8gj73drmpu186amn6a3f.apps.googleusercontent.com&as=-3e0a372fe569d5ed&destination=https%3A%2F%2Flogin.auth0.com&approval_state=!ChRmQmVlRTBVZ3JiVjEwd0F5dEx4aBIfWXdYcXJKbGhvcXdSTUpIMzhHRFhRN1R0QWpEMzRCVQ%E2%88%99AHw7d_cAAAAAWZ7flB_9_lrnXXSAxmwrLcHpgWHMlwJD&xsrfsig=AHgIfE9Fy3Nd3uZJ1VWUhgXaZbd6MdxLZA&flowName=GeneralOAuthFlow',
                          title='Order Entry')

    def clickAcctChosen(self):
        self.btnPickAcct.click()
        waitForAngular(self.driver)