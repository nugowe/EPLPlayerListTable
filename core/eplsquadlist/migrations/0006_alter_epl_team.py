# Generated by Django 4.2.7 on 2024-01-22 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eplsquadlist', '0005_alter_epl_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epl',
            name='Team',
            field=models.CharField(choices=[('Arsenal', 'Arsenal'), ('AstonVilla', 'Astonvilla'), ('Bournemouth', 'Bournemouth'), ('Brentford', 'Brentford'), ('Brighton', 'Brighton'), ('Burnley', 'Burnley'), ('Chelsea', 'Chelsea'), ('CrystalPalace', 'Crystalpalace'), ('Everton', 'Everton'), ('Fulham', 'Fulham'), ('Liverpool', 'Liverpool'), ('Luton', 'Luton'), ('ManchesterCity', 'Manchestercity'), ('ManchesterUnited', 'Manchesterunited'), ('NewcastleUnited', 'Newcastleunited'), ('NottingHamForest', 'Nottinghamforest'), ('ShieffieldUnited', 'Shieffieldunited'), ('TottenhamHotspur', 'Tottenhamhotspur'), ('WestHam', 'Westham'), ('Wolves', 'Wolves')], max_length=256),
        ),
    ]