# Generated by Django 3.2.4 on 2021-06-27 17:06

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoronaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('j_data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
