# Generated by Django 4.2.5 on 2023-11-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_category_user_categories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pref_game_categories',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='pref_game_categories',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='categories',
        ),
        migrations.AddField(
            model_name='user',
            name='pref_game_category',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Pref_game_categories',
        ),
    ]