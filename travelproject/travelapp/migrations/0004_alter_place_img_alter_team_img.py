# Generated by Django 4.2.2 on 2023-06-16 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_alter_place_img_alter_team_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='img',
            field=models.ImageField(height_field=60, upload_to='pics', width_field=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(height_field=60, upload_to='pics', width_field=50),
        ),
    ]
