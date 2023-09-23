from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='marakofr76@yandex.ru',
            first_name='Admin',
            last_name='Roman',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('13243546')
        user.save()
