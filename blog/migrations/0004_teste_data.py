# Generated by Django 4.0.5 on 2023-02-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_teste_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='teste',
            name='data',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
