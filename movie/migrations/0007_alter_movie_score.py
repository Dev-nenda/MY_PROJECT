# Generated by Django 4.2.2 on 2023-07-06 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_movie_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='score',
            field=models.FloatField(null=True),
        ),
    ]