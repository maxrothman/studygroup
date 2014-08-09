from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from studygroup.application import create_app, db
from studygroup.models import User
import settings

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def populate(debug=True):
  if debug:
    for m in settings.debug_records:
      db.session.add(m)
    db.session.commit()

if __name__ == "__main__":
    manager.run()
