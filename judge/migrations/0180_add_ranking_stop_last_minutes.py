# Generated by Django 2.2.28 on 2022-12-06 15:47

import django.core.validators
from django.db import migrations, models
import judge.models.profile


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0179_add_ranking_access_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='ranking_stop_last_minutes',
            field=models.IntegerField(default=0, help_text='If set, the public scoreboard will be stopped for the last X minutes.', verbose_name='ranking stop last minutes'),
        )
    ]
