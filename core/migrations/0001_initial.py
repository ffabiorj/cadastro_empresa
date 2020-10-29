# Generated by Django 2.2.16 on 2020-10-29 12:43

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
                ('nome_fantasia', models.CharField(blank=True, max_length=200, null=True)),
                ('cnpj', models.CharField(max_length=19)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('endereco', models.CharField(blank=True, max_length=100, null=True)),
                ('cidade', models.CharField(blank=True, max_length=20, null=True)),
                ('estado', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO'), ('DF', 'DF')], max_length=2, null=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('data_cadastro', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('A', 'Ativo'), ('I', 'Inativo')], max_length=6, null=True)),
                ('risco', models.CharField(blank=True, choices=[('AA', 'AA'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')], max_length=2, null=True)),
                ('agencia', models.CharField(blank=True, max_length=6, null=True)),
                ('conta', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'ordering': ['-nome_fantasia'],
            },
        ),
    ]
