# Generated by Django 3.1.1 on 2020-09-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='picture',
            field=models.ImageField(default=None, upload_to='employees/images/'),
        ),
    ]
