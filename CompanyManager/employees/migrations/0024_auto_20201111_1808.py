# Generated by Django 3.1.1 on 2020-11-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0023_auto_20201106_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeeType',
            field=models.CharField(choices=[('manager', 'Manager'), ('hourly', 'Hourly'), ('potential', 'Potential'), ('salaried', 'Salaried'), ('executive', 'Executive')], default='potential', max_length=20),
        ),
        migrations.AlterField(
            model_name='experience',
            name='text',
            field=models.TextField(blank=True, default='INSIDE EXPERIENCE TEXT'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='rank',
            field=models.CharField(choices=[('advanced', 'Advanced'), ('expert', 'Expert'), ('intermediate', 'Intermediate'), ('novice', 'Novice')], default='novice', max_length=50),
        ),
    ]
