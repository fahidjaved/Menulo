import sys, os
sys.path.insert(0, '/var/www/ssd1591/priv/menulo')
sys.path.insert(0, '/var/www/ssd1591/priv/venv/lib/python3.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'menulo.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()