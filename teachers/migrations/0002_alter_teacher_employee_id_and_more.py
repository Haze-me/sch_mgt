# Generated by Django 5.1.8 on 2025-04-30 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_alter_school_school_type'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='employee_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='teacher',
            unique_together={('school', 'employee_id')},
        ),
    ]
