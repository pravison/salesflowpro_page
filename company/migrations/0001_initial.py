# Generated by Django 5.0.1 on 2024-03-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('pitch', models.TextField(max_length=150)),
                ('address', models.TextField()),
                ('location', models.TextField()),
                ('county', models.TextField()),
                ('country', models.TextField()),
                ('phone', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=200)),
                ('branch_address', models.TextField(max_length=500)),
                ('location', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FrequentlyAskedQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=350)),
                ('answer', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='KeyPerfomanceIndicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KPI_name', models.CharField(max_length=200)),
                ('KPI_defination', models.TextField(max_length=500)),
                ('why_is_it_important', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=350)),
                ('product_price', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]