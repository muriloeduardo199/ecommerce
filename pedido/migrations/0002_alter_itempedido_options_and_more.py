# Generated by Django 4.1.2 on 2022-11-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itempedido',
            options={'verbose_name': 'Item do pedido', 'verbose_name_plural': 'Itens do pedido'},
        ),
        migrations.RenameField(
            model_name='itempedido',
            old_name='iamgem',
            new_name='imagem',
        ),
        migrations.AddField(
            model_name='itempedido',
            name='variacao',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itempedido',
            name='variacao_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='qtd_total',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]