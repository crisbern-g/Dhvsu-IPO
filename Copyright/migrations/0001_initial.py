# Generated by Django 4.0.3 on 2022-03-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CopyRightApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright_application_name', models.CharField(max_length=200)),
            ],
        ),
    ]
