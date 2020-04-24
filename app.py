import unittest

from flask import redirect, url_for, json
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api.v1 import blueprint_api_v1, api_v1
from api import create_app, db
from web import blueprint_web

app = create_app()
app.register_blueprint(blueprint_api_v1, url_prefix="/api/v1")
app.register_blueprint(blueprint_web, url_prefix="/")
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if app.config['SWAGGER_ENABLE'] == '1':
    @app.route("/swagger")
    def index_swagger():
        return redirect(url_for('api_v1.doc'))


@app.route("/")
def index():
    return redirect(url_for('web.views'))


@manager.command
def run():
    app.run(host=app.config['HOST'], port=app.config['PORT'])


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def swagger(action, filename):
    """Execute different actions about Swagger"""
    if action == 'export':
        with open(filename, 'w+') as file:
            file.write(json.dumps(api_v1.__schema__))


@manager.command
def list_routes():
    print(app.url_map)


if __name__ == '__main__':
    manager.run()
