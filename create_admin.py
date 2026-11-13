import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_shop.settings')
django.setup()

# Membuat akun admin baru secara paksa/reset password jika sudah ada
username = 'admin'
email = 'admin@example.com'
password = 'admin12345'

if User.objects.filter(username=username).exists():
    user = User.objects.get(username=username)
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print(f"Password untuk '{username}' berhasil diperbarui!")
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' berhasil dibuat!")
