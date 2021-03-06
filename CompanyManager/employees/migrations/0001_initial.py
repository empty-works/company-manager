# Generated by Django 3.1.1 on 2020-09-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=1000)),
                ('lastName', models.CharField(max_length=1000)),
                ('birthdate', models.DateField(blank=True)),
                ('address', models.CharField(max_length=2000)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
