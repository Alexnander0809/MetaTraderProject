# Generated by Django 4.1 on 2024-08-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_cedula_alter_cliente_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
