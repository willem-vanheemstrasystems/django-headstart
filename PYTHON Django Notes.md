PYTHON Django Notes:

To activate an environment that already exists, but we is not active, type from outside of the environment folder (e.g. django-headstart) the following:

source django-headstart/bin/activate

Notice that the command prompt now starts with (django-headstart), like so:

(django-headstart)Macintosh-8:python wvanheemstra$

The environment 'django-headstart' is now active, it (may) contains projects which you can go into, like so:

cd django-headstart/bin/django_test

In here is where we edit the settings file, inside the sub-folder (django-headstart/django_test/django_test):

cd django_test

settings.py

CREATING AN APP

To create an app (e.g. article) in our django_test project, from within the project folder (django-headstart/diango_test) type:

python manage.py startapp article




To deactivate an environment, from within the environment type:

deactivate

Notice that the command prompt now no longer starts with (django-headstart), but like so:

Macintosh-8:python wvanheemstra$
