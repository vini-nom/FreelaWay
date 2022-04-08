# Generated by Django 3.2.12 on 2022-04-08 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20220407_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('C', 'Em criação'), ('AA', 'Aguardando aprovação'), ('F', 'Finalizado')], default='C', max_length=2),
        ),
    ]
