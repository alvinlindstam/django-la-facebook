===========
README
===========

Dedicated facebook authentication for Django that does it via the backend and not javascript. Has lots of tests and a trivial-to-setup test project with working code.

Reason: http://pydanny.blogspot.com/2011/01/what-i-want-for-django-facebook-connect.html

Full Documentation: http://django-la-facebook.readthedocs.org/en/latest/index.html


Usage
-----

Get ``django-la-facebook`` into your python path::

    pip install django-la-facebook

Add ``la_facebook`` to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'la_facebook',
        ...
        )

Add ``la_facebook`` to your root urlconf (urls.py)::

    urlpatterns = patterns('',
        ...,
        url(r"^la_facebook/", include("la_facebook.urls")),
        ...,
    )

Add settings just as::

    FACEBOOK_ACCESS_SETTINGS = {
            "FACEBOOK_APP_ID": FACEBOOK_APP_ID,
            "FACEBOOK_APP_SECRET": FACEBOOK_APP_SECRET,
            # The following keys are optional
            # "CALLBACK": "la_facebook.callbacks.default.default_facebook_callback",
            # "PROVIDER_SCOPE": ['email','read_stream'],
            # "LOG_LEVEL": "DEBUG",
            # "LOG_FILE": "/tmp/la_facebook.log",
    }


Run tests
---------

Clone this repository::

    git clone https://github.com/EmilStenstrom/django-la-facebook.git .

Create a virtual environment so you don't polute your own (using virtualenv)::

    mkvirtualenv django-la-facebook

Install all the project requirements.txt::

    pip install -r requirements.txt

Run the provided tests::

    python test_project/manage.py test connect la_facebook

Rejoice!
