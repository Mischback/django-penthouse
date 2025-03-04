# SPDX-FileCopyrightText: 2025 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penthouse', '0022_alter_relic_bonus_type'),
    ]

    def add_relics(apps, schema_editor):
        Relic = apps.get_model("penthouse", "Relic")

        Relic.objects.create(
            name="Temporal Rift",
            rarity="RARE",
            bonus_type="CASHBO",
            bonus_value=2.0,
            source="E",
            condition="What Time is it? event; 350 medals"
        )
        Relic.objects.create(
            name="Dream Clock",
            rarity="EPIC",
            bonus_type="ORBSPD",
            bonus_value=5.0,
            source="E",
            condition="What Time is it? event; 700 medals"
        )
        Relic.objects.create(
            name="Hourglass",
            rarity="RARE",
            bonus_type="COINSB",
            bonus_value=2.0,
            source="E",
            condition="What Time is it? event (Boost relic); 550 medals"
        )
        Relic.objects.create(
            name="Time Compass",
            rarity="EPIC",
            bonus_type="ATKSPD",
            bonus_value=2.0,
            source="E",
            condition="What Time is it? event (Boost relic); 1100 medals"
        )

    def reverse(apps, schema_editor):
        pass

    operations = [
        migrations.RunPython(add_relics, reverse),
    ]


