import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_shop.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin12345')
    print("Superuser berhasil dibuat.")
else:
    print("Superuser sudah ada.")