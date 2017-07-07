from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from .testpageutilities.waitforangular import waitForAngular
from testutilities import Settings
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.command import Command


_LOCATOR_MAP = {'css': By.CSS_SELECTOR,
                'id_': By.ID,
                'name': By.NAME,
                'xpath': By.XPATH,
                'link_text': By.LINK_TEXT,
                'partial_link_text': By.PARTIAL_LINK_TEXT,
                'tag_name': By.TAG_NAME,
                'class_name': By.CLASS_NAME,
                }


# def WebElement_click(self):
#     """Clicks the element."""
#     print("my click")
#     time.sleep(Settings.SPEED)
#     self._execute(Command.CLICK_ELEMENT)
#
# WebElement.click = WebElement_click
#
#
# def WebElement_send_keys(self, keys):
#     """Clicks the element."""
#     print("my send_keys")
#     time.sleep(Settings.SPEED)
#     WebElement.send_keys(self, keys)
#
# WebElement.send_keys = WebElement_send_keys


# from selenium.webdriver.remote.webelement import WebElement as WBExt
#
# class newWB(object):
#     def __init__(self):
#         self._click = WBExt.click(self)
#
#     @classmethod
#     def new_click(self):
#         print('new click')
#         return self._click
#
#
# WebElement = newWB

class ExtWebElement(WebElement):

    def clickw(self):
        print('custom click')
        time.sleep(Settings.SPEED)
        # WebElement.click(self)
        self.click()

    def send_keysw(self, *value):
        print('custom send_keys')
        time.sleep(Settings.SPEED)
        # WebElement.click(self)
        self.send_keys(*value)


class PageElement(object):
    """Page Element descriptor.
    :param css:    `str`
        Use this css locator
    :param id_:    `str`
        Use this element ID locator
    :param name:    `str`
        Use this element name locator
    :param xpath:    `str`
        Use this xpath locator
    :param link_text:    `str`
        Use this link text locator
    :param partial_link_text:    `str`
        Use this partial link text locator
    :param tag_name:    `str`
        Use this tag name locator
    :param class_name:    `str`
        Use this class locator
    :param context: `bool`
        This element is expected to be called with context
    Page Elements are used to access elements on a page. The are constructed
    using this factory method to specify the locator for the element.
        >>> from page_objects import PageObject, PageElement
        >>> class MyPage(PageObject):
                elem1 = PageElement(css='div.myclass')
                elem2 = PageElement(id_='foo')
                elem_with_context = PageElement(name='bar', context=True)
    Page Elements act as property descriptors for their Page Object, you can get
    and set them as normal attributes.
    """

    def __init__(self, context=False, **kwargs):
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        k, v = next(iter(kwargs.items()))
        self.locator = (_LOCATOR_MAP[k], v)
        self.has_context = bool(context)

    def find(self, context):
        try:
            if Settings.ISANGULAR:
                waitForAngular(context)

            # f = context.find_element(*self.locator)
            # return MyWebElem(f)

            return context.find_element(*self.locator)
        except NoSuchElementException:
            return None

    def __get__(self, instance, owner, context=None):
        # print('get: ' + str(self.__dict__['locator'][1]))  # prints the locator of the element TODO: add to verbose logging
        # print(str(type(instance)))
        # print(str(type(owner)))
        # print(str(type(context)))
        if not instance:
            return None
        if not context and self.has_context:
            return lambda ctx: self.__get__(instance, owner, context=ctx)

        if not context:
            context = instance.driver

        # return self.find(context)
        f = self.find(context)
        f.__class__ = ExtWebElement
        return f

    def __set__(self, instance, value):
        if self.has_context:
            raise ValueError(
                "Sorry, the set descriptor doesn't support elements with context.")
        elem = self.__get__(instance, instance.__class__)
        if not elem:
            raise ValueError("Can't set value, element not found")
        elem.send_keys(value)
        assert elem.get_attribute("value") == value

    def activate(self):
        pass

    # def click(self):
    #     print('custom clicking')
    #     self.click()


    # not currently working
    # def assertFound(self):
    #     if self is None:
    #         print('Element Not Found!')

