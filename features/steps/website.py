from behave import *
from selenium import webdriver
import time


@given('我们打开浏览器')
def step_impl(context):
    pass


@when(u'输入主页网址"{text}"')
def step_impl(context, text):
    #    if text not in context.response:
    #        fail('%r not in %r' % (text, context.response))
    #    time.sleep(5)
    context.browser.get(text)
    time.sleep(5)


@then('我们看到页标题"{text}"')
def step_impl(context, text):
    #    if text not in context.response:
    #        fail('%r not in %r' % (text, context.response))
    print(context.response)
    assert text in context.browser.title
