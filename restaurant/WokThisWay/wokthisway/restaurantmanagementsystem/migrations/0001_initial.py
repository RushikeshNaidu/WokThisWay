# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('ID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('course', models.CharField(max_length=50)),
                ('cuisine', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]