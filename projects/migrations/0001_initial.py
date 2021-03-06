# Generated by Django 3.1.12 on 2021-06-18 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creators', '0001_initial'),
        ('locations', '0001_initial'),
        ('categories', '0001_initial'),
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
                ('state_changed_at', models.DateTimeField(null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='creators.creator')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='locations.location')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='categories.subcategory')),
            ],
        ),
    ]
