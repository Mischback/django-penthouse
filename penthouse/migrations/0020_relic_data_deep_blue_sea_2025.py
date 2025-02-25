# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penthouse', '0019_alter_relic_bonus_type'),
    ]

    def add_relics(apps, schema_editor):
        Relic = apps.get_model("penthouse", "Relic")

        Relic.objects.create(
            name="Coral Crown",
            rarity="RARE",
            bonus_type="HREGEN",
            bonus_value=2.0,
            source="E",
            condition="Deep Blue Sea event (2025); 350 medals"
        )
        Relic.objects.create(
            name="Angler Fish",
            rarity="EPIC",
            bonus_type="THORNS",
            bonus_value=2.0,
            source="E",
            condition="Deep Blue Sea event (2025); 700 medals"
        )

    def reverse(apps, schema_editor):
        pass

    operations = [
        migrations.RunPython(add_relics, reverse),
    ]


