# Generated by Django 4.1.4 on 2022-12-19 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_staff_name_alter_staff_bio_alter_staff_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('send_date', models.DateField(auto_now_add=True, verbose_name='')),
                ('role', models.CharField(choices=[('S', 'sécretaire'), ('D', 'directeur'), ('RCL1I', 'responsable de concours licence informatique'), ('RCM1I', 'responsable de concours master 1 informatique'), ('RCINGI', 'responsable de concours ingenieur informatique')], max_length=100, null=True)),
                ('note', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.CharField(choices=[('S', 'sécretaire'), ('D', 'directeur'), ('RCL1I', 'responsable de concours licence informatique'), ('RCM1I', 'responsable de concours master 1 informatique'), ('RCINGI', 'responsable de concours ingenieur informatique')], max_length=50),
        ),
    ]
