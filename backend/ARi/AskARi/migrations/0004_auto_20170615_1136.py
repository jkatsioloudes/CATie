# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AskARi', '0003_auto_20170615_1115'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='followup',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='followup',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='followup',
            name='poster',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='id_per_parent',
            new_name='id_per_question',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='AskARi.Comment'),
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('parent', 'id_per_question')]),
        ),
        migrations.DeleteModel(
            name='FollowUp',
        ),
    ]
