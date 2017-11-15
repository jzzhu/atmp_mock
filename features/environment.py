from behave import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_all(context):
    #context.browser = webdriver.Firefox()
    context.browser = webdriver.Remote(
        command_executor='http://hub:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)


def after_all(context):
    context.browser.close()


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass
