# Generated by Django 3.2.13 on 2023-02-05 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_catalogo_sexo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenDesconto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=12, unique=True)),
                ('used', models.BooleanField(default=False)),
                ('dt_inclusao', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
