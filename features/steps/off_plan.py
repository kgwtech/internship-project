from behave import *

""" Calls methods from the Page Object for Reelly.io Off-PlanPage """

@then("Click on the first product")
def click_product(context):
    context.app.off_plan.click_first_product()