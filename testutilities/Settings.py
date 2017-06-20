from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


####################
# BROWSER SETTINGS #
####################

BROWSER = DesiredCapabilities.CHROME

# used by driver.set_window_size(300, 500)
WINDOWSIZE = [1300, 1000]

SELENIUMADDRESS = 'http://127.0.0.1:4445/wd/hub'







###################
# TIMING SETTINGS #
###################

#TODO: add stuff here




########################
# ENVIRONMENT SETTINGS #
########################

ENVIRONMENT = 'https://qa1.wealthforge.org'





#######################
# CHANGEABLE SETTINGS #
#######################

# If this is not set to false on a page that is not angular, the element.find() will break on the waitForAngular
ISANGULAR = True