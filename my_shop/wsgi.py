import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_shop.settings')

# Trik otomatis membuat database saat server pertama kali berjalan di Render
try:
    from django.core.management import call_command
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Migration error: {e}")

application = get_wsgi_application()
