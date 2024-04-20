import os

from flask_script import Manager

from src import blueprint
from src import createApp

app = createApp(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run(debug=True)


if __name__ == '__main__':
    manager.run()

app.run()
