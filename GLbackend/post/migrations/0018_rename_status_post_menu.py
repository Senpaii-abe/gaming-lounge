# Generated by Django 4.2.5 on 2023-11-20 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_post_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='status',
            new_name='menu',
        ),
    ]
