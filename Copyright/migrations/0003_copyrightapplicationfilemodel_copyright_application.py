# Generated by Django 4.0.3 on 2022-03-25 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Copyright', '0002_copyrightapplicationfilemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='copyrightapplicationfilemodel',
            name='copyright_application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Copyright.copyrightapplicationmodel'),
        ),
    ]