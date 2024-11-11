elefanto_pytest_plugins = [
    "sphinx.testing.fixtures",
    "tests.fixtures",
]


def pytest_configure(config):
    for plugin_module in elefanto_pytest_plugins:
        config.pluginmanager.import_plugin(plugin_module)
