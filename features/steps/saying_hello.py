from behave import given, when, then

@given("we have flask working")
def step_impl(context):
    pass

@when("we hit the root path")
def step_impl(context):
    context.page = context.client.get('/')
    assert context.page
    assert context.page.status_code == 200

@then("we see the Hello World regard")
def step_impl(context):
    print(context.page.text)
    assert context.page.text == "<p>Hello, World!</p>"