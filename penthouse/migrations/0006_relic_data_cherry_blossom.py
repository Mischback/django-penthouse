# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penthouse', '0005_add_initial_relic_data'),
    ]

    def add_relics(apps, schema_editor):
        Relic = apps.get_model("penthouse", "Relic")

        Relic.objects.create(
            name="Koi Fish",
            rarity="RARE",
            bonus_type="LABSPD",
            bonus_value=2.0,
            source="E",
            condition="Cherry Blossom event 2024; 350 medals"
        )
        Relic.objects.create(
            name="Bonsai Tree",
            rarity="EPIC",
            bonus_type="COINSB",
            bonus_value=5.0,
            source="E",
            condition="Cherry Blossom event 2024; 700 medals"
        )
        Relic.objects.create(
            name="Tea Ceremony",
            rarity="RARE",
            bonus_type="HEALTH",
            bonus_value=2.0,
            source="E",
            condition="Cherry Blossom event 2024; purchasable for 200 medals"
        )
        Relic.objects.create(
            name="Kimono",
            rarity="EPIC",
            bonus_type="COINSB",
            bonus_value=5.0,
            source="E",
            condition="Cherry Blossom event 2024; purchasable for 500 medals"
        )

    def reverse(apps, schema_editor):
        pass

    operations = [
        migrations.RunPython(add_relics, reverse),
    ]


