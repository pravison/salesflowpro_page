# Generated by Django 5.0.1 on 2024-04-28 11:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0011_rename_email_customer_email'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interaction',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='customerlabel',
            name='colour',
            field=models.CharField(choices=[('primary', 'blue'), ('white', 'white '), ('light', 'light grey'), ('dark', 'black'), ('warning', 'yellow'), ('danger', 'red'), ('secondary', 'grey'), ('success', 'green '), ('info', 'sky blue ')], default='light', max_length=70),
        ),
        migrations.AlterField(
            model_name='customer',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lead_type',
            field=models.CharField(choices=[('hot', 'hot'), ('cold', 'cold'), ('warm', 'warm')], max_length=20),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customer'),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='next_step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.probablenextstep'),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='outcome',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.probableconversationoutcome'),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customer'),
        ),
    ]