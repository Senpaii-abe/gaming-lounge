# Generated by Django 4.2.5 on 2023-11-11 20:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_user_pref_game_titles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pref_game_titles',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
