# Generated by Django 3.1.12 on 2021-06-16 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('backers', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('goal', models.FloatField()),
                ('pledged', models.FloatField()),
                ('usd_pledged', models.FloatField()),
                ('currency', models.CharField(max_length=3)),
                ('launched_at', models.DateTimeField()),
                ('state', models.CharField(max_length=255)),
            ],
        ),
    ]