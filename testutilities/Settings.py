from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



####################
# BROWSER SETTINGS #
####################

browser = DesiredCapabilities.CHROME

# used by driver.set_window_size(300, 500)
windowSize = [1300, 1000]

seleniumAddress = 'http://127.0.0.1:4445/wd/hub'



###################
# TIMING SETTINGS #
###################

#TODO: add stuff here