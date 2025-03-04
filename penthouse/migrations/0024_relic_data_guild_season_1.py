# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penthouse', '0023_relic_data_what_time_is_it'),
    ]

    def add_relics(apps, schema_editor):
        Relic = apps.get_model("penthouse", "Relic")

        Relic.objects.create(
            name="Throne",
            rarity="RARE",
            bonus_type="HEALTH",
            bonus_value=2.0,
            source="E",
            condition="Guild Season 1; 75 tokens"
        )
        Relic.objects.create(
            name="Crown",
            rarity="EPIC",
            bonus_type="CRITFA",
            bonus_value=5.0,
            source="E",
            condition="Guild Season 1; 150 tokens"
        )

    def reverse(apps, schema_editor):
        pass

    operations = [
        migrations.RunPython(add_relics, reverse),
    ]


