import os

def settings(config):
    INSTALLED_APPS = list(config['INSTALLED_APPS'])
    for app in [
            'social_django',
            'django_otp',
            'django_otp.plugins.otp_static',
            'django_otp.plugins.otp_totp',
            'two_factor.apps.TwoFactorConfig',
            'django_social_oauth_two_factor.apps.Config',
    ]:
        if app not in INSTALLED_APPS:
            INSTALLED_APPS.append(app)
    config['INSTALLED_APPS'] = tuple(INSTALLED_APPS)

    MIDDLEWARE = list(config['MIDDLEWARE'])
    for mware in [
            'django_otp.middleware.OTPMiddleware',
            'two_factor.middleware.threadlocals.ThreadLocals',
            #'django_social_oauth_two_factor.middleware.TwoFactorMiddleware',
    ]:
        if mware not in MIDDLEWARE:
            MIDDLEWARE.append(mware)
    config['MIDDLEWARE'] = list(MIDDLEWARE)

    AUTHENTICATION_BACKENDS = list(config.get('AUTHENTICATION_BACKENDS',
                                              ['django.contrib.auth.backends.ModelBackend']))
    for backend in [
            'social_core.backends.google.GoogleOAuth2',
    ]:
        if backend not in AUTHENTICATION_BACKENDS:
            AUTHENTICATION_BACKENDS.append(backend)
    config['AUTHENTICATION_BACKENDS'] = list(AUTHENTICATION_BACKENDS)

    for env_key in [
            'TWILIO_ACCOUNT_SID',
            'TWILIO_AUTH_TOKEN',
            'TWILIO_CALLER_ID',
            'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY',
            'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET',
            'SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS',
    ]:
        if env_key not in config:
            if env_key == 'SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS':
                config[env_key] = os.environ.get(env_key, '').split(',')
            else:
                config[env_key] = os.environ.get(env_key)

    cfg = {
        'LOGIN_URL': '/login/google-oauth2/',
        'TWO_FACTOR_SMS_GATEWAY': 'two_factor.gateways.twilio.gateway.Twilio',
        'TWO_FACTOR_CALL_GATEWAY': 'two_factor.gateways.twilio.gateway.Twilio',
        'TWO_FACTOR_PATCH_ADMIN': False,
    }

    config.update(**cfg)

    config['ORIGINAL_ROOT_URLCONF'] = config.get('ROOT_URLCONF')
    config['ROOT_URLCONF'] = 'django_social_oauth_two_factor.urls'
