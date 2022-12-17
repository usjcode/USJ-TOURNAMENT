# Generated by Django 4.1.4 on 2022-12-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_staff_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='bio',
            field=models.TextField(default='do you know ngdream likes banana ???'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.CharField(choices=[('S', 'sécretaire'), ('D', 'directeur'), ('RCL1I', 'responsable de concours licence 1 informatique'), ('RCM1I', 'responsable de concours master 1 informatique'), ('RCINGI', 'responsable de concours ingenieur informatique')], max_length=50),
        ),
    ]