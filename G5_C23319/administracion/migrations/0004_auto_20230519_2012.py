# Generated by Django 3.2.18 on 2023-05-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_alter_naturalpark_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campsite',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='naturalpark',
            name='image',
            field=models.ImageField(upload_to='imagenes/'),
        ),
    ]
