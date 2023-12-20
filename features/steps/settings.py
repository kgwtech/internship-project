from behave import *

""" Calls methods from the Page Object for Reelly.io Settings Page """

@then("Click on 'Contact us' option")
def click_contact_us(context):
    context.app.settings.click_contact_us()