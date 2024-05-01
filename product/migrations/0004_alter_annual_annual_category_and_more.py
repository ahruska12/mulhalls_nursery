# Generated by Django 4.2.10 on 2024-05-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_plant_plant_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annual',
            name='annual_category',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='plant_picture',
            field=models.ImageField(default='default/default_plant.png', upload_to='plants/'),
        ),
    ]
