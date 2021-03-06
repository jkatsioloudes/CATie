# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0002_auto_20170613_1543'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=4000)),
                ('score', models.IntegerField()),
                ('id_per_parent', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=4000)),
                ('score', models.IntegerField()),
                ('id_per_parent', models.PositiveIntegerField()),
                ('parent_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ARiProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=4000)),
                ('id_per_lecture', models.IntegerField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecture.Lecture')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ARiProfile')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AskARi.Question'),
        ),
        migrations.AddField(
            model_name='comment',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ARiProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('parent', 'id_per_lecture')]),
        ),
        migrations.AlterUniqueTogether(
            name='followup',
            unique_together=set([('content_type', 'parent_id', 'id_per_parent')]),
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('parent', 'id_per_parent')]),
        ),
    ]
