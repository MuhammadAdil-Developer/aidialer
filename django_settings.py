# fastapi_project/django_settings.py
import os
import sys

# Assuming your Django project is one directory above your FastAPI project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'VoiceFusion'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VoiceFusion.settings')

import django
django.setup()
