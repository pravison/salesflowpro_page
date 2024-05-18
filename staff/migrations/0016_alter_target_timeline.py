# Generated by Django 5.0.1 on 2024-05-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0015_alter_target_timeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='timeline',
            field=models.CharField(choices=[('This Week', 'This Week'), ('This Month', 'This Month'), ('This Year', 'This Year'), ('Today', 'Today')], default='TODAY', max_length=100),
        ),
    ]
