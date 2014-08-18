from django.core.management.base import BaseCommand, CommandError
from nazs import modules


class Command(BaseCommand):
    help = 'Save a module conf files'

    def handle(self, *args, **kwargs):
        names = [n.upper() for n in args]
        for module in modules():
            if module.name.upper() in names:
                if module.enabled:
                    module.save()
                    names.remove(module.name.upper())

                else:
                    raise CommandError('Module %s is disabled' % module.name)

        if names:
            raise CommandError('Module %s does not exist' % ','.join(names))
