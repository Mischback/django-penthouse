# Generated by Django 5.1.1 on 2024-10-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penthouse', '0002_run'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='duration',
            field=models.PositiveIntegerField(default=1, help_text='Duration of the run (in seconds)', verbose_name='Duration'),
        ),
    ]
