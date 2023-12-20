from behave import *

""" Calls methods from the Page Object for Reelly.io Main Page """

@given("Open the main page")
def open_main(context):
    context.app.main.open_main()

@then("Click 'Open in browser' button")
def click_open_browser_btn(context):
    context.app.main.click_open_browser_btn()