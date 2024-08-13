"""
WSGI config for cuppa_cake project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'cuppa_cake' project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cuppa_cake.settings")

# Get the WSGI application for the project
application = get_wsgi_application()
