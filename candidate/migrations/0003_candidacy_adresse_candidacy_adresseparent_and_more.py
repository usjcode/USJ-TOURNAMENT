# Generated by Django 4.1.4 on 2023-01-15 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_noteo_rename_note_notee_remove_candidate_tournaments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidacy',
            name='adresse',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='adresseparent',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='bacc',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='baccmark',
            field=models.IntegerField(default=10, verbose_name='moyenne générale au bacc'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='birth_place',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='candidate.candidate'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='examcenter',
            field=models.CharField(default='yaoundé', max_length=100, verbose_name="centre d'examination"),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='exschool',
            field=models.CharField(max_length=100, null=True, verbose_name='votre établissement'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='exschoolcity',
            field=models.CharField(max_length=100, null=True, verbose_name='ville de votre établissement'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='hasrepeated',
            field=models.BooleanField(default=False, verbose_name='avez vous déja redoublé ?'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='mention',
            field=models.CharField(default='passable', max_length=100),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='nombreenfant',
            field=models.IntegerField(default=1, verbose_name="nombre d'enfant"),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='nombreenfantes',
            field=models.IntegerField(default=0, verbose_name="nombre d'enfant en etudes superieur"),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='nommere',
            field=models.CharField(max_length=100, null=True, verbose_name='nom du pere'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='nompere',
            field=models.CharField(max_length=100, null=True, verbose_name='nom de la mere'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='obtentionyear',
            field=models.IntegerField(default=2022, null=True, verbose_name="année d'obtention"),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='probatoiremark',
            field=models.IntegerField(default=10, verbose_name='moyenne générale au probatoire'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='professionmere',
            field=models.CharField(max_length=100, null=True, verbose_name='profession de la mere'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='professionpere',
            field=models.CharField(max_length=100, null=True, verbose_name='profession du père'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='region',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='repeatedclasse',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='series',
            field=models.CharField(default='E', max_length=10, verbose_name='votre série'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='situation',
            field=models.CharField(default='mariées', max_length=100),
        ),
        migrations.AlterField(
            model_name='candidacy',
            name='cni_number',
            field=models.CharField(max_length=1000, null=True, verbose_name='numéro de cni'),
        ),
        migrations.AlterField(
            model_name='candidacy',
            name='phone',
            field=models.CharField(max_length=100, null=True, verbose_name='téléphone'),
        ),
    ]