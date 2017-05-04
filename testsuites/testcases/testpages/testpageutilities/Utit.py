from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0


class Utit:

    # from http://stackoverflow.com/a/33813953/5454556
    # if this does not work well enough, try the other answers here
    def waitForAngular(driver):
        # driver = webdriver.Chrome()

        WebDriverWait(driver, 10).until(
            lambda s: driver.execute_script(
                "return (window.angular !== undefined) && (angular.element(document).injector() !== undefined) && (angular.element(document).injector().get('$http').pendingRequests.length === 0)")
        )

