from accounts.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Create a root user'

    def handle(self, *args, **options):
        # Create a root user
        try:
            user = User.objects.get_or_create(username='root',email='root@root.root',
                                       is_superuser=True, is_staff=True, is_active=True, is_email_verified=True)
            user.set_password('root')
            user.save()

        except Exception as e:
            print(e)
            print('Root user already exists')
            return