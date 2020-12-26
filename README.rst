==============================
Django Social OAuth Two Factor
==============================


.. image:: https://img.shields.io/pypi/v/django_social_oauth_two_factor.svg
        :target: https://pypi.python.org/pypi/django_social_oauth_two_factor

.. image:: https://img.shields.io/travis/ejucovy/django_social_oauth_two_factor.svg
        :target: https://travis-ci.com/ejucovy/django_social_oauth_two_factor

.. image:: https://readthedocs.org/projects/django-social-oauth-two-factor/badge/?version=latest
        :target: https://django-social-oauth-two-factor.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Log in to a Django site with social oauth (e.g. Google/Facebook) and optionally enforced two-factor


* Free software: MIT license
* Documentation: https://django-social-oauth-two-factor.readthedocs.io.


Setup
-----

Add all of the following to your INSTALLED_APPS:

    'social_django',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor.apps.TwoFactorConfig',
    'social_django_two_factor.apps.Config',

Add all of the following to your MIDDLEWARE:

    'django_otp.middleware.OTPMiddleware',
    'two_factor.middleware.threadlocals.ThreadLocals',
    'social_django_two_factor.middleware.Admin2FAMiddleware',

Your AUTHENTICATION_BACKENDS should look like this:

    AUTHENTICATION_BACKENDS = [
        'social_core.backends.google.GoogleOAuth2',
        'django.contrib.auth.backends.ModelBackend',
    ]

Use the following two_factor settings:

    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    TWILIO_CALLER_ID = os.environ.get('TWILIO_CALLER_ID')

    TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'
    TWO_FACTOR_CALL_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'
    TWO_FACTOR_PATCH_ADMIN = False

Use the following social_django settings:

    LOGIN_URL = '/login/google-oauth2/'
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ['GOOGLE_OAUTH_KEY']
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ['GOOGLE_OAUTH_SECRET']
    SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = os.environ['GOOGLE_OAUTH_ALLOWED_DOMAINS'].split(',')

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
