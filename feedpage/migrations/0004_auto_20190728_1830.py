# Generated by Django 2.2.3 on 2019-07-28 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedpage', '0003_auto_20190728_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sunny',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedpage.Feed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rainy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedpage.Feed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cloudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedpage.Feed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='cloudy_users',
            field=models.ManyToManyField(blank=True, related_name='feeds_cloudy', through='feedpage.Cloudy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feed',
            name='rainy_users',
            field=models.ManyToManyField(blank=True, related_name='feeds_rainy', through='feedpage.Rainy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feed',
            name='sunny_users',
            field=models.ManyToManyField(blank=True, related_name='feeds_sunny', through='feedpage.Sunny', to=settings.AUTH_USER_MODEL),
        ),
    ]
