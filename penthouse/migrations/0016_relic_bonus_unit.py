# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penthouse', '0015_alter_metadata_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='relic',
            name='bonus_unit',
            field=models.CharField(default='%', help_text='Unit of the bonus value', max_length=3, verbose_name='Bonus Unit'),
        ),
    ]
