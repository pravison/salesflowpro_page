# Generated by Django 5.0.1 on 2024-04-14 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_alter_customer_lead_type_and_more'),
        ('staff', '0002_pipeline_important_alter_pipeline_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipeline',
            name='postponed_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='target',
            name='timeline',
            field=models.CharField(choices=[('TY', 'This Year'), ('TW', 'This Week'), ('TM', 'This Month'), ('TODAY', 'Today')], default='TODAY', max_length=100),
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(max_length=5000)),
                ('pipeline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]