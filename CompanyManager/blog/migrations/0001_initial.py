# Generated by Django 3.1.1 on 2020-10-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=3000)),
                ('postDate', models.DateField()),
                ('text', models.TextField()),
            ],
        ),
    ]
