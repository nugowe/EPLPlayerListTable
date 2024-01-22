import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from eplsquadlist.models import EPL


class Command(BaseCommand):
    help = "Loads car data from CSV file"

    def handle(self, *args, **options):
        datafile = settings.BASE_DIR / 'data' / 'EPLPLAYERROASTER1.csv'

        with open(datafile) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                EPL.objects.get_or_create(Position=row[0], PlayerName=row[1], Nation=row[2], Team=row[3])

