import django.utils.timezone
from django.db import models
from datetime import date

from django.db.models.signals import post_save
from django.dispatch import receiver


class Plant(models.Model):
    plant_id = models.AutoField(primary_key=True)
    add_date = models.DateField(default=date.today())
    plant_type = models.CharField(max_length=10)
    plant_name = models.CharField(max_length=30, blank=True, null=True)
    plant_size = models.CharField(max_length=30, blank=True, null=True)
    plant_color = models.CharField(max_length=30, blank=True, null=True)
    plant_description = models.CharField(max_length=1000, blank=True, null=True)
    plant_picture = models.ImageField(upload_to="plants/", default="default/default_plant.png")
    department = models.ForeignKey('user.Department', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.plant_name

    class Meta:
        db_table = 'plant'


class Annual(models.Model):
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE, primary_key=True)
    is_hardy = models.BooleanField(blank=True, null=True)
    is_semi_hardy = models.BooleanField(blank=True, null=True)
    shade_tolerant = models.BooleanField(blank=True, null=True)
    heat_tolerant = models.BooleanField(blank=True, null=True)
    drought_tolerant = models.BooleanField(blank=True, null=True)
    annual_category = models.CharField(blank=True, null=True, max_length=100)

    class Meta:
        db_table = 'annual'


class Perennial(models.Model):
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE, primary_key=True)
    light_code = models.CharField(max_length=30, blank=True, null=True)
    moisture_level = models.CharField(max_length=30, blank=True, null=True)
    care_level = models.CharField(max_length=30, blank=True, null=True)
    perennial_category = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'perennial'


class Shrub(models.Model):
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE, primary_key=True)
    shrub_category = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'shrub'


class Tree(models.Model):
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE, primary_key=True)
    tree_category = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'tree'
