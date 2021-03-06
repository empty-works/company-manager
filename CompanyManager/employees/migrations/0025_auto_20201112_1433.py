# Generated by Django 3.1.1 on 2020-11-12 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employees', '0024_auto_20201111_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='recorded_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeeType',
            field=models.CharField(choices=[('manager', 'Manager'), ('executive', 'Executive'), ('potential', 'Potential'), ('salaried', 'Salaried'), ('hourly', 'Hourly')], default='potential', max_length=20),
        ),
        migrations.AlterField(
            model_name='skill',
            name='rank',
            field=models.CharField(choices=[('intermediate', 'Intermediate'), ('expert', 'Expert'), ('novice', 'Novice'), ('advanced', 'Advanced')], default='novice', max_length=50),
        ),
    ]
