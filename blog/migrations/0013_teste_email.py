# Generated by Django 4.0.5 on 2023-02-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_teste_bairro_remove_teste_celular_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teste',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
