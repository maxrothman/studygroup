from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from studygroup.application import create_app, db
import studygroup.models as models

import settings

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def populate(debug=True):
  if debug:
    for i in settings.debug_records:
      record = models.__dict__[i[0]](**i[1])
      db.session.add(record)
    db.session.commit()

if __name__ == "__main__":
    manager.run()
