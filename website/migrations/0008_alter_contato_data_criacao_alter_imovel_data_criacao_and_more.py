# Generated by Django 5.0.7 on 2024-08-30 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_bairro_ishomepage_alter_contato_data_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 30, 12, 26, 58, 657899), null=True),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 30, 12, 26, 58, 657367), null=True),
        ),
        migrations.AlterField(
            model_name='imovelcontato',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 30, 12, 26, 58, 657899), null=True),
        ),
    ]
