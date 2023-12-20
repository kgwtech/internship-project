from behave import *

""" Calls methods from the Page Object for Reelly.io Partner Sub Pages """

@then("Verify the 'Contact us' page opened")
def verify_contact_us_opened(context):
    context.app.partner_sub_pages.verify_contact_us_opened()

@then("Verify there are at least {number} social media icons (Contact us)")
def verify_contact_us_social_icons(context, number):
    context.app.partner_sub_pages.verify_contact_us_social_icons(number)