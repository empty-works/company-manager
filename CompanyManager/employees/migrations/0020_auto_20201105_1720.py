# Generated by Django 3.1.1 on 2020-11-05 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0019_auto_20201102_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SkillsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeeType',
            field=models.CharField(choices=[('executive', 'Executive'), ('potential', 'Potential'), ('hourly', 'Hourly'), ('salaried', 'Salaried'), ('manager', 'Manager')], default='potential', max_length=20),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.skillslist')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.experiencelist')),
            ],
        ),
    ]
