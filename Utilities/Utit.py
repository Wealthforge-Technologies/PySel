from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium import webdriver


class Utit:
    
    def waitForAngular(driver):
        # driver = webdriver.Chrome()

        WebDriverWait(driver, 10).until(
            lambda s: driver.execute_script(
                "return (window.angular !== undefined) && (angular.element(document).injector() !== undefined) && (angular.element(document).injector().get('$http').pendingRequests.length === 0)")
        )




# import org.openqa.selenium.JavascriptExecutor;
# import org.openqa.selenium.WebDriver;
# import org.openqa.selenium.support.ui.ExpectedCondition;
#
# public class AdditionalConditions {
#     public static ExpectedCondition<Boolean> angularHasFinishedProcessing() {
#         return new ExpectedCondition<Boolean>() {
#             @Override
#             public Boolean apply(WebDriver driver) {
#                 return Boolean.valueOf(((JavascriptExecutor) driver).executeScript("return (window.angular !== undefined) && (angular.element(document).injector() !== undefined) && (angular.element(document).injector().get('$http').pendingRequests.length === 0)").toString());
#             }
#         };
#     }
# }
