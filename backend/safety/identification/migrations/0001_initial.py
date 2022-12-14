# Generated by Django 3.2.5 on 2022-09-01 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('currency', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('secondary_email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('fax_number', models.CharField(max_length=10, unique=True)),
                ('limit_of_debt', models.FloatField()),
                ('balance', models.FloatField()),
                ('payment_terms', models.TextField()),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identification.coin')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identification.paymentmethod')),
            ],
        ),
    ]
