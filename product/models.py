from django.db import models


class Plant(models.Model):
    PLANT_TYPES = [
        ('Shrub', 'Shrub'),
        ('Tree', 'Tree'),
        ('Annual', 'Annual'),
        ('Perennial', 'Perennial'),
    ]
    plant_id = models.AutoField(primary_key=True)
    plant_type = models.CharField(max_length=10, choices=PLANT_TYPES)
    plant_name = models.CharField(max_length=30, blank=True, null=True)
    plant_size = models.CharField(max_length=30, blank=True, null=True)
    plant_color = models.CharField(max_length=30, blank=True, null=True)
    plant_description = models.CharField(max_length=1000, blank=True, null=True)
    plant_picture = models.CharField(max_length=300, blank=True, null=True)
    department = models.ForeignKey('user.Department', on_delete=models.CASCADE, blank=True, null=True)

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
    annual_category = models.BooleanField(blank=True, null=True)

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
