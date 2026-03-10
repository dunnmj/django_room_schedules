from django.conf import settings

API_KEY = getattr(settings, 'ARTIFAX_API_KEY', False)
if not API_KEY:
    raise Exception("ARTIFAX_API_KEY not set in settings.py")

BASE_ADDRESS = getattr(settings, 'ARTIFAX_BASE_ADDRESS', False)
if not BASE_ADDRESS:
    raise Exception("ARTIFAX_BASE_ADDRESS not set in settings.py")
HOUR_BREAK_POINT = getattr(settings, 'HOUR_BREAK_POINT', 4)