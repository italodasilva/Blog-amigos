# Generated by Django 4.0.5 on 2023-02-14 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_cpf_alter_customer_bairro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='CPF',
            field=models.CharField(help_text='Coloque dessa maneira: 000.000.000-00', max_length=14, null=True, unique=True, verbose_name='DIGITE O SEU CPF:'),
        ),
    ]
