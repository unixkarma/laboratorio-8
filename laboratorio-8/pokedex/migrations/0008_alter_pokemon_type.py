# Generated by Django 4.2 on 2024-08-02 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0007_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('T', 'Tierra'), ('A', 'Agua'), ('P', 'Planta'), ('E', 'Eléctrica'), ('R', 'Reptil'), ('F', 'Fuego')], max_length=30),
        ),
    ]
