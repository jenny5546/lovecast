# Generated by Django 2.2.3 on 2019-08-15 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedpage', '0047_profile_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='feed_photos',
            field=models.ManyToManyField(null=True, related_name='feed_photo', to='feedpage.Photos'),
        ),
    ]
