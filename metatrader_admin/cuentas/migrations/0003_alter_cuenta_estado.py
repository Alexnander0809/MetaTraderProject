# Generated by Django 4.1 on 2024-08-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_cuenta_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='estado',
            field=models.CharField(max_length=20),
        ),
    ]