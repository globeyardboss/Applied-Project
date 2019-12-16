# Generated by Django 2.1 on 2018-08-23 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20180823_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_degrees',
            name='Degree_Acronym',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee_degrees',
            name='Degree_Name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employment_history',
            name='Job_Step',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employment_history',
            name='Job_Title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personal_information',
            name='First_Name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='qualifications_on_entry',
            name='Level_Attained',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
