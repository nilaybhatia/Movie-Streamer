# Generated by Django 2.2.11 on 2020-03-31 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streamer_app', '0003_auto_20200331_0327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='published_date',
            new_name='published_datetime',
        ),
    ]