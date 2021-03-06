# Generated by Django 3.1.1 on 2020-10-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20201015_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employeeType',
            field=models.CharField(choices=[('4', 'Manager'), ('2', 'Hourly'), ('3', 'Salaried'), ('5', 'Executive'), ('1', 'Potential')], default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='wage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
