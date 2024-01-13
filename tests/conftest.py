
from widget_server import config as app_config


### https://docs.pytest.org/en/7.1.x/example/simple.html#detect-if-running-from-within-a-pytest-run
def pytest_configure(config):
    app_config.IS_TEST = True
