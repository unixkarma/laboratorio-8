# Generated by Django 4.2 on 2024-08-02 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0009_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('T', 'Tierra'), ('F', 'Fuego'), ('R', 'Reptil'), ('A', 'Agua'), ('P', 'Planta'), ('E', 'Eléctrica')], max_length=30),
        ),
    ]
