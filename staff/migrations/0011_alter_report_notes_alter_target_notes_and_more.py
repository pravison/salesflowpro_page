# Generated by Django 5.0.1 on 2024-04-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0010_staff_phone_alter_target_timeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='notes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='target',
            name='notes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='target',
            name='timeline',
            field=models.CharField(choices=[('This Year', 'This Year'), ('Today', 'Today'), ('This Month', 'This Month'), ('This Week', 'This Week')], default='TODAY', max_length=100),
        ),
    ]
