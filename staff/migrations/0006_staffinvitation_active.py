# Generated by Django 4.1.4 on 2022-12-19 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_staffinvitation_alter_staff_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffinvitation',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
