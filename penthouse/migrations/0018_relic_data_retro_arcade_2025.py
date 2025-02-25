# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penthouse', '0017_alter_relic_bonus_type'),
    ]

    def add_relics(apps, schema_editor):
        Relic = apps.get_model("penthouse", "Relic")

        Relic.objects.create(
            name="Power Glove",
            rarity="RARE",
            bonus_type="DAMAGE",
            bonus_value=2.0,
            source="E",
            condition="Retro Arcade event (2025); 350 medals"
        )
        Relic.objects.create(
            name="Arcade Token",
            rarity="EPIC",
            bonus_type="BOTRNG",
            bonus_value=2.0,
            bonus_unit="m",
            source="E",
            condition="Retro Arcade event (2025); 700 medals"
        )

    def reverse(apps, schema_editor):
        pass

    operations = [
        migrations.RunPython(add_relics, reverse),
    ]


