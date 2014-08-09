studygroup
==========

Prototype application to allow creation of study groups within a given Meetup
group.


Developing
==========

You will run your development machine so that it pretends to be
"dev-studygroup.bostonpython.com":

1. [Create](http://virtualenv.readthedocs.org/en/latest/virtualenv.html#usage)
    a virtualenv named venv and
    [activate](http://virtualenv.readthedocs.org/en/latest/virtualenv.html#activate-script) it. 
    ([Install virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation) 
    if you haven't already.)

2. Install the requirements:

        $ pip install -r requirements.txt

3. Create a settings_local.py alongside settings.py, with details from the
    OAuth consumer you just created and any database records you want added.
    For those, the format is `('model_name', {arg1:val, arg2:val, ...})`

        SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/studygroup.db"

        debug_models = [
            ('User', dict(id=0, meetup_member_id=0, full_name ="Debug Admin", is_admin=True)),
            ('User', dict(id=1, meetup_member_id=1, full_name ="Debug User", is_admin=False)),
        ]

4. Create the database tables:

        $ python manage.py db upgrade

4. Populate the database with the records you listed in settings_local.py:

        $ python manage.py populate

5. Start the server:

        $ python run_server.py -p 8080

6. To sign in, go a URL of this form in your browser: 

        `http://localhost:8080/debug_login?id=<user_id>`

###Optional: set up OAuth

Study Group uses OAuth authentication with meetup.com, so to test
that functionality you will need to do a few extra steps.

1. Go to http://www.meetup.com/meetup_api/, and click "OAuth Consumers".

2. Create a new consumer, with these details:

        Consumer Name: Boston Python Study Groups (Dev)
        Redirect URI: http://localhost:8080/

3. Add the following to your setttings_local.py:

        MEETUP_GROUP_ID = 469457    # Boston Python, use this exactly.
        MEETUP_OAUTH_KEY = "esgls3vaf5k7d9ufrvj0jtuvo0"     # Fill in with your own key
        MEETUP_OAUTH_SECRET = "mgi9mlaagc24o8a3f4hcvu0mb0"  #   .. and secret.

7. If you click the Sign In Now button, it should take you to meetup.com and
    ask you to authorize Boston Python Study Groups.

Running tests
=============

Tests are run with unittest in the standard library:

        $ python -m unittest discover

