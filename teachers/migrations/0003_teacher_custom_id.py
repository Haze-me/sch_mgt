# Generated by Django 5.1.8 on 2025-05-02 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_alter_teacher_employee_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='custom_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
