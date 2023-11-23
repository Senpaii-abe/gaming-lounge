# Generated by Django 4.2.5 on 2023-11-12 14:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_remove_user_pref_game_titles'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pref_game_titles_updated',
            field=models.ManyToManyField(blank=True, related_name='pref_game_titles_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
