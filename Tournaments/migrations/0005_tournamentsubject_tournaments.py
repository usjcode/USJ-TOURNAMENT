# Generated by Django 4.1.4 on 2023-03-18 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tournaments', '0004_remove_tournamentsubject_tournaments'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentsubject',
            name='tournaments',
            field=models.ManyToManyField(to='Tournaments.tournamenttype'),
        ),
    ]
