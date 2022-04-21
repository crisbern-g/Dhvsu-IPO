# Generated by Django 4.0.3 on 2022-04-05 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Copyright', '0013_alter_copyrightapplicationfilemodel_copyright_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authoridsfilemodel',
            name='copyright_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Copyright.copyrightapplicationmodel'),
        ),
        migrations.AlterField(
            model_name='certificateofregistrationfilemodel',
            name='copyright_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Copyright.copyrightapplicationmodel'),
        ),
        migrations.AlterField(
            model_name='deedofassignmentfilemodel',
            name='copyright_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deed_of_assignment', to='Copyright.copyrightapplicationmodel'),
        ),
        migrations.AlterField(
            model_name='electroniccopyfilemodel',
            name='copyright_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Copyright.copyrightapplicationmodel'),
        ),
        migrations.AlterField(
            model_name='memorandumofappointmentfilemodel',
            name='copyright_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Copyright.copyrightapplicationmodel'),
        ),
    ]
