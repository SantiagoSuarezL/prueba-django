# Generated by Django 5.1 on 2024-08-16 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='comprado',
            new_name='marcado',
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='producto',
            name='lista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='prueba.lista'),
        ),
    ]
