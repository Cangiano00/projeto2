# Generated by Django 5.1.2 on 2024-11-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0007_alter_historia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='categoria',
            field=models.ManyToManyField(to='historias.category'),
        ),
    ]
