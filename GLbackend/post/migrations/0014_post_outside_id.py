# Generated by Django 4.2.5 on 2023-11-20 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_alter_gametitle_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='outside_id',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
