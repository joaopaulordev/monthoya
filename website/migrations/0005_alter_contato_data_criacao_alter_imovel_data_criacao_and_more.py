# Generated by Django 5.0.7 on 2024-07-21 03:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_contato_data_criacao_alter_imovel_data_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 21, 0, 6, 26, 43466), null=True),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 21, 0, 6, 26, 42472), null=True),
        ),
        migrations.AlterField(
            model_name='imovelcontato',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 21, 0, 6, 26, 43466), null=True),
        ),
    ]
