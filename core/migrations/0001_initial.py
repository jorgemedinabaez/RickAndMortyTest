# Generated by Django 4.2.2 on 2023-06-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Personaje",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200, verbose_name="Nombre")),
                ("status", models.CharField(max_length=200, verbose_name="Estado")),
                ("species", models.CharField(max_length=200, verbose_name="Especie")),
                ("gender", models.CharField(max_length=200, verbose_name="Género")),
                ("image", models.URLField(verbose_name="URL imagen")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
