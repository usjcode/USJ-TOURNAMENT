# Generated by Django 4.1.4 on 2023-03-18 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tournaments', '0006_remove_writingsession_tournament_delete_oralsession_and_more'),
        ('candidate', '0002_oralnote_writingnote_remove_noteo_candidat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oralnote',
            name='date',
        ),
        migrations.RemoveField(
            model_name='oralnote',
            name='tournament',
        ),
        migrations.RemoveField(
            model_name='writingnote',
            name='date',
        ),
        migrations.RemoveField(
            model_name='writingnote',
            name='observation',
        ),
        migrations.RemoveField(
            model_name='writingnote',
            name='tournament',
        ),
        migrations.AddField(
            model_name='oralnote',
            name='observation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='writingnote',
            name='matiere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Tournaments.tournamentsubject'),
        ),
        migrations.AlterField(
            model_name='oralnote',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='candidate.candidacy'),
        ),
    ]
