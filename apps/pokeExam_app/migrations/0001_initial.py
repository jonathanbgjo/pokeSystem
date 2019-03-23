# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-28 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginReg_app', '0002_auto_20170928_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gave', to='loginReg_app.User')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='got', to='loginReg_app.User')),
            ],
        ),
    ]