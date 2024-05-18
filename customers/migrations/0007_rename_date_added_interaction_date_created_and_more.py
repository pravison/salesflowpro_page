# Generated by Django 5.0.1 on 2024-04-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_interaction_next_step_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interaction',
            old_name='date_added',
            new_name='date_created',
        ),
        migrations.AlterField(
            model_name='customer',
            name='lead_type',
            field=models.CharField(choices=[('warm', 'warm'), ('cold', 'cold'), ('hot', 'hot')], max_length=20),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='conversation_method',
            field=models.CharField(choices=[('call', 'call'), ('chat', 'chat'), ('face', 'face to face ')], max_length=70),
        ),
    ]