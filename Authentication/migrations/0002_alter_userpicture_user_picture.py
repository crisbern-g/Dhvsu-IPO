# Generated by Django 4.0.3 on 2022-04-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpicture',
            name='user_picture',
            field=models.ImageField(upload_to='user_picture'),
        ),
    ]
