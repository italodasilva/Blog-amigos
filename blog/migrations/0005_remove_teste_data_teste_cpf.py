# Generated by Django 4.0.5 on 2023-02-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_teste_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teste',
            name='data',
        ),
        migrations.AddField(
            model_name='teste',
            name='CPF',
            field=models.CharField(max_length=14, null=True),
        ),
    ]
