# Generated by Django 4.0.5 on 2022-06-21 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ISSN', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='editorialmodel',
            old_name='mark_file',
            new_name='editorial_file',
        ),
        migrations.RenameField(
            model_name='journalmodel',
            old_name='application_form_file',
            new_name='journal_file',
        ),
    ]
