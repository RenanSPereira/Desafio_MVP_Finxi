# Generated by Django 3.1.1 on 2020-09-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demanda',
            name='status_finalizacao',
            field=models.BooleanField(default=False),
        ),
    ]
