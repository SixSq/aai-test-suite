def pytest_addoption(parser):
    parser.addoption("--username", action="store", default="ocre-test", dest="username")
    parser.addoption("--password", action="store", default=None, dest="_password")


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.username
    if 'username' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("username", [option_value])

    option_value = metafunc.config.option._password
    if '_password' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("_password", [option_value])
