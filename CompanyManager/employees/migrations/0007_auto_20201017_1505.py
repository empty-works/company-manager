# Generated by Django 3.1.1 on 2020-10-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20201016_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeeType',
            field=models.CharField(choices=[('5', 'Executive'), ('3', 'Salaried'), ('1', 'Potential'), ('4', 'Manager'), ('2', 'Hourly')], default='1', max_length=20),
        ),
    ]