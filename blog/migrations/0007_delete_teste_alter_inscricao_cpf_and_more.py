# Generated by Django 4.0.5 on 2023-02-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_teste_sexo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teste',
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='CPF',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='bairro',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='celular',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='cep',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='cidade',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='complemento',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='email',
            field=models.EmailField(max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='estado',
            field=models.CharField(choices=[('ACRE', 'AC'), ('ALAGOAS', 'AL'), ('AMAPÁ', 'AP'), ('AMAZONAS', 'AM'), ('BAHIA', 'BA'), ('CEARÁ', 'CE'), ('DISTRITO FEDERAL', 'DF'), ('ESPÍRITO SANTO', 'ES'), ('GOIÁS', 'GO'), ('MARANHÃO', 'MA'), ('MATO GROSSO', 'MT'), ('MATO GROSSO DO SUL', 'MS'), ('MINAS GERAIS', 'MG'), ('PARÁ', 'PA'), ('PARAÍBA', 'PB'), ('PARANÁ', 'PR'), ('PERNAMBUCO', 'PE'), ('PIAUÍ', 'PI'), ('RIO DE JANEIRO', 'RJ'), ('RIO GRANDE DO NORTE', 'RN'), ('RIO GRANDE DO SUL', 'RS'), ('RONDÔNIA', 'RO'), ('RORÔIMA', 'RR'), ('SANTA CATARINA', 'SC'), ('SÃO PAULO', 'SP'), ('SERGIPE', 'SE'), ('TOCÂNTIS', 'TO')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='nascimento',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='nome',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='numero',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='pcd',
            field=models.CharField(choices=[('SIM', 'sim'), ('NÃO', 'Não')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='rua',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='sexo',
            field=models.CharField(choices=[('MASCULINO', 'Masculino'), ('FEMININO', 'Feminino')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='sobrenome',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
