# Generated by Django 2.2.16 on 2020-10-27 22:59

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=200)),
                ('nome_fantasia', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=14, validators=[core.validators.validate_cnpj])),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=5)),
                ('telefone', models.CharField(max_length=15)),
                ('data_cadastro', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('risco', models.CharField(choices=[('AA', 'AA'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')], max_length=2)),
                ('agencia', models.CharField(max_length=6)),
                ('conta', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['-nome_fantasia'],
            },
        ),
    ]