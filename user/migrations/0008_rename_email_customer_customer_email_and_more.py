# Generated by Django 4.2.10 on 2024-03-25 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_customer_email_customer_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='email',
            new_name='customer_email',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='email',
            new_name='employee_email',
        ),
    ]
