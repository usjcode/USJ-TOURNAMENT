# Generated by Django 4.1.4 on 2023-01-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0006_rename_birth_place_candidacy_lieu de naissance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidacy',
            name='lieu de naissance',
        ),
        migrations.AddField(
            model_name='candidacy',
            name='birth_place',
            field=models.CharField(max_length=100, null=True, verbose_name='lieu de naissance'),
        ),
    ]