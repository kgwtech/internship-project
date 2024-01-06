from behave import *

""" Calls methods from the Page Object for Reelly.io Off-Plan Sub Pages Page """

@then("Verify the three options of visualization are 'architecture', 'interior', 'lobby'")
def verify_visualisations(context):
    context.app.off_plan_sub_pages.verify_visualisations()

@then("Verify the visualization options are clickable")
def click_visualisations(context):
    context.app.off_plan_sub_pages.click_visualisations()