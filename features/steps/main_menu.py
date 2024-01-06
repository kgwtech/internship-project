import time

from behave import *

""" Calls methods from the Page Object for Reelly.io Main Menu Page """

@then("Verify user in signed in")
def verify_sign_in(context):
    context.app.main_menu.verify_sign_in()

@then("Click on 'settings' option")
def click_settings_option(context):
    context.app.main_menu.click_settings_option()

@then("Click on 'off plan' at the left side menu")
def click_off_plan(context):
    context.app.main_menu.click_off_plan_option()

