# Generated by Django 4.2.5 on 2023-12-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0005_alter_command_task_alter_command_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_image',
            field=models.ImageField(blank=True, upload_to='task_cover', verbose_name='task_image'),
        ),
    ]