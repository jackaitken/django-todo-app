# Generated by Django 3.1.6 on 2021-02-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0008_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
    ]
