# Generated by Django 4.2 on 2024-07-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('T', 'Tierra'), ('E', 'Eléctrica'), ('F', 'Fuego'), ('A', 'Agua'), ('P', 'Planta'), ('R', 'Reptil')], max_length=30),
        ),
    ]
