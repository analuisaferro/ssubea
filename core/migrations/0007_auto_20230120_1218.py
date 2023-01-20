# Generated by Django 3.2.13 on 2023-01-20 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230118_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='nome',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Nome/apelido'),
        ),
        migrations.AlterField(
            model_name='ave',
            name='anilha',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Código da anilha'),
        ),
        migrations.AlterField(
            model_name='ave',
            name='animal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.animal'),
        ),
        migrations.AlterField(
            model_name='ave',
            name='especie',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Espécie'),
        ),
    ]
