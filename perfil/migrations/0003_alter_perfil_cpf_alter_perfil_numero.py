# Generated by Django 4.1.2 on 2022-11-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_alter_perfil_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='numero',
            field=models.CharField(max_length=5),
        ),
    ]
