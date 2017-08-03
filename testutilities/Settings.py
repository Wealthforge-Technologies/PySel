from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


####################
# BROWSER SETTINGS #
####################

BROWSER = DesiredCapabilities.CHROME

# used by driver.set_window_size(300, 500)
WINDOWSIZE = [1300, 1000]

SELENIUMADDRESS = 'http://127.0.0.1:4445/wd/hub'








####################
# LOGGING SETTINGS #
####################

MAX_VERBOSE = 10
MED_VERBOSE = 5
NOT_VERBOSE = 0

VERBOSITY = NOT_VERBOSE


###################
# TIMING SETTINGS #
###################


SPEED_DEFAULT = 0
SPEED_FAST = 0.1
SPEED_HUMAN = 0.5
SPEED_HUMAN_SLOW = 1.0

SPEED = SPEED_HUMAN_SLOW


########################
# ENVIRONMENT SETTINGS #
########################

ENVIRONMENT = 'https://qa1.wealthforge.org'





#######################
# CHANGEABLE SETTINGS #
#######################

# If this is not set to false on a page that is not angular, the element.find() will break on the waitForAngular
ISANGULAR = True