# Generated by Django 4.2.7 on 2023-11-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_charisma_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]