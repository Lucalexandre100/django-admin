# Generated by Django 2.1.2 on 2018-10-31 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefone',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
            preserve_default=False,
        ),
    ]
