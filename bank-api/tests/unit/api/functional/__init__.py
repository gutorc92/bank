import pytest
from app import create_app


@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['pt_BR']

@pytest.fixture(autouse=True, scope="module")
def headers():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    return headers

@pytest.fixture(autouse=True, scope="module")
def client():
    """Configures the app for testing
    Sets app config variable ``TESTING`` to ``True``
    :return: App for testing
    """

    flask_app = create_app()
    flask_app.config['TESTING'] = True

    print('passou aqui')

    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!
