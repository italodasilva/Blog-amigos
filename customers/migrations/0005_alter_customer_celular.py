# Generated by Django 4.0.5 on 2023-02-14 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_alter_customer_cpf_alter_customer_celular_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='celular',
            field=models.CharField(help_text='Coloque o DDD em ( ) : Ex: (31)99999-9999', max_length=14, null=True, verbose_name='DIGITE O NÚMERO DO SEU CELULAR:'),
        ),
    ]
