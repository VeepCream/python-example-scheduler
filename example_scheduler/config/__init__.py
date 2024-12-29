import os

app_env = os.getenv('APP_ENV', 'DEVELOPMENT')


if app_env == 'PRODUCTION':
    from .production import *
else:
    from .development import *
