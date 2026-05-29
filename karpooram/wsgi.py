# """
# WSGI config for karpooram project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "karpooram.settings")

# application = get_wsgi_application()


"""
WSGI config for karpooram project.
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Add the project directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'karpooram.settings')

# For Vercel
app = get_wsgi_application()