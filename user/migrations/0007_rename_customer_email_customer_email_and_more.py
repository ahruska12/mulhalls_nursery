# Generated by Django 4.2.10 on 2024-03-25 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_employee_employee_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_email',
            new_name='email',
        ),
        migrations.AlterModelTable(
            name='customerlogin',
            table='customer_login_history',
        ),
        migrations.CreateModel(
            name='EmployeeLogin',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('login_token', models.CharField(max_length=400)),
                ('date', models.DateField(null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.employee')),
            ],
            options={
                'db_table': 'employee_login_history',
            },
        ),
    ]
