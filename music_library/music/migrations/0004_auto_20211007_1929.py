# Generated by Django 3.2.7 on 2021-10-08 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20211007_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='release_date',
        ),
        migrations.AddField(
            model_name='song',
            name='release_year',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]
