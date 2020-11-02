# Generated by Django 3.1.1 on 2020-11-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0014_auto_20201102_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeeType',
            field=models.CharField(choices=[('salaried', 'Salaried'), ('executive', 'Executive'), ('potential', 'Potential'), ('manager', 'Manager'), ('hourly', 'Hourly')], default='potential', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='employees/images/'),
        ),
    ]
