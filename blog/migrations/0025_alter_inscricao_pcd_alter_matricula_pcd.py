# Generated by Django 4.0.5 on 2023-02-12 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_matricula_complemento_matricula_pcd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='pcd',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='pcd',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não')], max_length=3, null=True),
        ),
    ]