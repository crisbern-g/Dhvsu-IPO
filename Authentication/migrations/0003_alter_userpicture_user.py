# Generated by Django 4.0.3 on 2022-04-27 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Authentication', '0002_alter_userpicture_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpicture',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_picture', to=settings.AUTH_USER_MODEL),
        ),
    ]
