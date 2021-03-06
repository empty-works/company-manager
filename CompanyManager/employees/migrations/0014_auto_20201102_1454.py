# Generated by Django 3.1.1 on 2020-11-02 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0013_auto_20201101_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeeType',
            field=models.CharField(choices=[('executive', 'Executive'), ('manager', 'Manager'), ('hourly', 'Hourly'), ('potential', 'Potential'), ('salaried', 'Salaried')], default='potential', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.ImageField(blank=True, default=None, upload_to='employees/images/'),
        ),
    ]
