# Generated by Django 4.2.2 on 2023-07-16 09:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_product_date_of_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 16, 13, 38, 8, 11915), null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 16, 13, 38, 8, 11915), null=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(max_length=50, verbose_name='номер версии')),
                ('version_name', models.CharField(max_length=50, verbose_name='название версии')),
                ('version_is_active', models.BooleanField()),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
