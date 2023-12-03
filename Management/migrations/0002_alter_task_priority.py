# Generated by Django 4.2.5 on 2023-11-22 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], max_length=20, verbose_name='priority'),
        ),
    ]
