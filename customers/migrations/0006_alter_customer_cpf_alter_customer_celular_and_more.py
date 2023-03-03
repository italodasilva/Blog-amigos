# Generated by Django 4.0.5 on 2023-02-14 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_customer_celular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='CPF',
            field=models.CharField(max_length=14, null=True, unique=True, verbose_name='DIGITE O SEU CPF:'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='celular',
            field=models.CharField(max_length=14, null=True, verbose_name='DIGITE O NÚMERO DO SEU CELULAR:'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='nascimento',
            field=models.CharField(max_length=10, null=True, verbose_name='INFORME SUA DATA DE NASCIMENTO:'),
        ),
    ]