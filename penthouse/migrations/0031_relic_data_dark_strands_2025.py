# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penthouse', '0030_alter_relic_bonus_type'),
    ]

    def add_relics(apps, schema_editor):
        Relic = apps.get_model("penthouse", "Relic")

        Relic.objects.create(
            name="Haunted Mirror",
            rarity="RARE",
            bonus_type="WALLRE",
            bonus_value=2.0,
            bonus_unit="s",
            source="E",
            condition="Dark Strands event (2025); 350 medals"
        )
        Relic.objects.create(
            name="Shadow Puppet",
            rarity="EPIC",
            bonus_type="SCRITM",
            bonus_value=5.0,
            source="E",
            condition="Dark Strands event (2025); 700 medals"
        )
        Relic.objects.create(
            name="Whispering Web",
            rarity="RARE",
            bonus_type="FDEFUP",
            bonus_value=1.0,
            source="E",
            condition="Dark Strands event (2025, Boost relic); 550 medals"
        )
        Relic.objects.create(
            name="Cursed Candle",
            rarity="EPIC",
            bonus_type="SCRITC",
            bonus_value=2.0,
            source="E",
            condition="Dark Strands event (2025, Boost relic); 1100 medals"
        )

    def reverse(apps, schema_editor):
        pass

    operations = [
        migrations.RunPython(add_relics, reverse),
    ]


