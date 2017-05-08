import os
import unittest
# class for handling a set of commands
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app

# initialize the app with all its configurations
app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)
# create an instance of class that will handle our commands
manager = Manager(app)

# Define the migration command to always be preceded by the word "db"
# Example usage: python manage.py db init
manager.add_command('db', MigrateCommand)


# define our command for testing called "test"
# Usage: python manage.py test
@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('./tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
