# Generated by Django 5.0.6 on 2024-06-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_rename_employee_expensereport_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensereport',
            name='date',
            field=models.DateField(blank=True, help_text='today date.', null=True),
        ),
    ]
