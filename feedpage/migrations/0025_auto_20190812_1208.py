# Generated by Django 2.2.3 on 2019-08-12 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedpage', '0024_feed_hashtags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='hashtags',
            new_name='hashtag_str',
        ),
    ]
