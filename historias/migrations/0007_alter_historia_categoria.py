# Generated by Django 5.1.2 on 2024-11-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0006_category_historia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='categoria',
            field=models.ManyToManyField(related_name='categoria', to='historias.category'),
        ),
    ]
