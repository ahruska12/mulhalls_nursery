from django.db import models
from product.models import Plant


class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.department_name

    class Meta:
        db_table = 'department'


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_first_name = models.CharField(max_length=30, blank=True, null=True)
    employee_last_name = models.CharField(max_length=30, blank=True, null=True)
    employee_password = models.CharField(max_length=30, blank=True, null=True)
    is_admin = models.CharField(max_length=1, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.employee_first_name + " " + self.employee_last_name

    class Meta:
        db_table = 'employee'


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_first_name = models.CharField(max_length=30, blank=True, null=True)
    customer_last_name = models.CharField(max_length=30, blank=True, null=True)
    customer_email = models.CharField(max_length=30, blank=True, null=True)
    customer_password = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.customer_first_name + " " + self.customer_last_name

    class Meta:
        db_table = 'customer'


class SearchHistory(models.Model):
    search_id = models.IntegerField(primary_key=True)
    search_date = models.DateField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Date: {self.search_date}, Plant: {self.plant}"

    class Meta:
        db_table = 'search_history'


class QuestionsAsked(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question_date = models.DateField(blank=True, null=True)
    question = models.CharField(max_length=1000, blank=True, null=True)
    answer = models.CharField(max_length=1000, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.question_id

    class Meta:
        db_table = 'questions_asked'
