# Generated by Django 3.0.5 on 2020-04-07 16:48

from django.db import migrations
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='country',
            field=django_countries.fields.CountryField(default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]
