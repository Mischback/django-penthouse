# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penthouse', '0012_alter_relic_bonus_type'),
    ]

    def add_relics(apps, schema_editor):
        Relic = apps.get_model("penthouse", "Relic")

        Relic.objects.create(
            name="Falling Apple",
            rarity="RARE",
            bonus_type="FDEFUP",
            bonus_value=1.0,
            source="E",
            condition="Gravity event; 350 medals"
        )
        Relic.objects.create(
            name="3 Body Solution",
            rarity="EPIC",
            bonus_type="SCRITC",
            bonus_value=2.0,
            source="E",
            condition="Gravity event; 700 medals"
        )

    def reverse(apps, schema_editor):
        pass

    operations = [
        migrations.RunPython(add_relics, reverse),
    ]


