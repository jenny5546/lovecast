# Generated by Django 2.2.3 on 2019-08-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedpage', '0048_auto_20190815_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='result',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
