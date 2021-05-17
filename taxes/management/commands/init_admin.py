from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Utility to create a superuser'

    def _create_admin(self, username: str = None, email: str = None, password: str = None) -> None:
        if not User.objects.count():
            if username and email and password:
                self.stdout.write(self.style.SUCCESS(f'Creating account for {username} ({email})'))
                try:
                    User.objects.create_superuser(username=username, email=email, password=password)
                    self.stdout.write(self.style.SUCCESS('DONE'))
                except ValueError as error:
                    self.stderr.write(self.style.ERROR(error))
            else:
                self.stderr.write(
                    self.style.ERROR(
                        'The following arguments are required: -u/--username, -e/--email, -p/--password'))
        else:
            self.stderr.write(self.style.WARNING('Admin accounts can only be initialized if no Accounts exist'))

    def handle(self, *args, **options) -> None:

        self.stdout.write(self.help)

        username = 'admin'
        email = 'admin@admin.com'
        password = 'admin1234'

        self._create_admin(username, email, password)
