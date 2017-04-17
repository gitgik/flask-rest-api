
class BaseConfig(object):
    """Base configuration class."""

    DATABASE_URL = 'sqlite://:memory:'
    SECRET = 'some-very-long-string-of-characters'


class DevelopmentConfig(BaseConfig):
    """This class represents configurations for Development."""

    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """This class represents configurations for Production."""

    DEBUG = False
    TESTING = False
