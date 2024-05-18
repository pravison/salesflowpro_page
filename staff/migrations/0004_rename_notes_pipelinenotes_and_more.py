# Generated by Django 5.0.1 on 2024-04-14 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_alter_pipeline_postponed_counter_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notes',
            new_name='PipelineNotes',
        ),
        migrations.AlterField(
            model_name='pipelinenotes',
            name='pipeline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.pipeline'),
        ),
        migrations.AlterField(
            model_name='target',
            name='timeline',
            field=models.CharField(choices=[('TODAY', 'Today'), ('TM', 'This Month'), ('TW', 'This Week'), ('TY', 'This Year')], default='TODAY', max_length=100),
        ),
    ]