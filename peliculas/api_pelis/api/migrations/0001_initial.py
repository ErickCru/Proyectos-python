# Generated by Django 3.0.4 on 2020-03-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('estreno', models.IntegerField(default=2000)),
                ('imagen', models.URLField(help_text='De imdb mismo')),
                ('resumen', models.TextField(help_text='Descripción corta')),
            ],
            options={
                'ordering': ['titulo'],
            },
        ),
    ]
