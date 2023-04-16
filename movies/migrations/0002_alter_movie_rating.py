# Generated by Django 4.2 on 2023-04-16 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(choices=[('Rated G', 'G'), ('Rated PG', 'Pg'), ('Rated PG-13', 'Pg13'), ('Rated R', 'R'), ('Rated NC-17', 'Nc17')], default='Rated G', max_length=20),
        ),
    ]
