# Generated by Django 3.1.1 on 2020-11-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0022_auto_20201106_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='from_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='to_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='skill',
            name='rank',
            field=models.CharField(choices=[('expert', 'Expert'), ('intermediate', 'Intermediate'), ('novice', 'Novice'), ('advanced', 'Advanced')], default='novice', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeeType',
            field=models.CharField(choices=[('potential', 'Potential'), ('salaried', 'Salaried'), ('executive', 'Executive'), ('manager', 'Manager'), ('hourly', 'Hourly')], default='potential', max_length=20),
        ),
    ]
