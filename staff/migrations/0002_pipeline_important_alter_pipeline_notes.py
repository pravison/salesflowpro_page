# Generated by Django 5.0.1 on 2024-04-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipeline',
            name='important',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pipeline',
            name='notes',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]