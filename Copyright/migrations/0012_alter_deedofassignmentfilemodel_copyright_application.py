# Generated by Django 4.0.3 on 2022-04-04 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Copyright', '0011_alter_copyrightapplicationfilemodel_copyright_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deedofassignmentfilemodel',
            name='copyright_application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deed_of_assignment', to='Copyright.copyrightapplicationmodel'),
        ),
    ]
