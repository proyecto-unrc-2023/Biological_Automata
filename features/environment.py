from behave import fixture, use_fixture
from app import create_app
from models.logic.GameController import GameController, Game_Mode


@fixture
def empire_client(context, *args, **kwargs):
    app = create_app("testing")
    app.testing = True

    context.client = app.test_client()

    ctx = app.test_request_context()
    ctx.push()

    yield context.client

    ctx.pop()

def before_feature(context, feature):
    # -- HINT: Recreate a new flaskr client before each feature is executed.
    use_fixture(empire_client, context)

@fixture
def initial(context):
    context.game = GameController()
    context.game.set_mode(Game_Mode.ANTIBIOTIC)
    context.game.config(6,6)
    
def before_scenario(context, scenario):
    use_fixture(initial, context)