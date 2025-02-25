# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penthouse', '0004_remove_profile_relics_relic_claimed_by'),
    ]

    def init_relics(apps, schema_editor):
        Relic = apps.get_model("penthouse", "Relic")

        # Milestones
        Relic.objects.create(
            name="T:I Flux",
            rarity="RARE",
            bonus_type="COINSB",
            bonus_value=2.0,
            source="M",
            condition="Tier 1, Wave 4.500"
        )
        Relic.objects.create(
            name="T:II Lumin",
            rarity="RARE",
            bonus_type="LABSPD",
            bonus_value=1.5,
            source="M",
            condition="Tier 2, Wave 4.500"
        )
        Relic.objects.create(
            name="T:III Pulse",
            rarity="RARE",
            bonus_type="CRITFA",
            bonus_value=2.0,
            source="M",
            condition="Tier 3, Wave 4.500"
        )
        Relic.objects.create(
            name="T:IV Harmonic",
            rarity="RARE",
            bonus_type="DAMAGE",
            bonus_value=2.0,
            source="M",
            condition="Tier 4, Wave 4.500"
        )
        Relic.objects.create(
            name="T:V Ether",
            rarity="RARE",
            bonus_type="HEALTH",
            bonus_value=2.0,
            source="M",
            condition="Tier 5, Wave 4.500"
        )
        Relic.objects.create(
            name="T:VI Nova",
            rarity="EPIC",
            bonus_type="DEFABS",
            bonus_value=5.0,
            source="M",
            condition="Tier 6, Wave 4.500"
        )
        Relic.objects.create(
            name="T:VII Aether",
            rarity="EPIC",
            bonus_type="COINSB",
            bonus_value=5.0,
            source="M",
            condition="Tier 7, Wave 4.500"
        )
        Relic.objects.create(
            name="T:VIII Graviton",
            rarity="EPIC",
            bonus_type="DMGPME",
            bonus_value=5.0,
            source="M",
            condition="Tier 8, Wave 4.500"
        )
        Relic.objects.create(
            name="T:IX Fusion",
            rarity="EPIC",
            bonus_type="HEALTH",
            bonus_value=5.0,
            source="M",
            condition="Tier 9, Wave 4.500"
        )
        Relic.objects.create(
            name="T:X Plasma",
            rarity="EPIC",
            bonus_type="DMGPME",
            bonus_value=5.0,
            source="M",
            condition="Tier 10, Wave 4.500"
        )
        Relic.objects.create(
            name="T:XI Resonance",
            rarity="LEGEND",
            bonus_type="DEFABS",
            bonus_value=10.0,
            source="M",
            condition="Tier 11, Wave 4.500"
        )
        Relic.objects.create(
            name="T:XII Chrono",
            rarity="LEGEND",
            bonus_type="LABSPD",
            bonus_value=10.0,
            source="M",
            condition="Tier 12, Wave 4.500"
        )
        Relic.objects.create(
            name="T:XIII Hyper",
            rarity="LEGEND",
            bonus_type="COINSB",
            bonus_value=10.0,
            source="M",
            condition="Tier 13, Wave 4.500"
        )
        Relic.objects.create(
            name="T:XIV Arcane",
            rarity="LEGEND",
            bonus_type="DAMAGE",
            bonus_value=10.0,
            source="M",
            condition="Tier 14, Wave 4.500"
        )
        Relic.objects.create(
            name="T:XV Celestial",
            rarity="LEGEND",
            bonus_type="CRITFA",
            bonus_value=10.0,
            source="M",
            condition="Tier 15, Wave 4.500"
        )
        Relic.objects.create(
            name="T:XVI Quantum",
            rarity="LEGEND",
            bonus_type="HEALTH",
            bonus_value=10.0,
            source="M",
            condition="Tier 16, Wave 4.500"
        )
        Relic.objects.create(
            name="T:XVII Nebula",
            rarity="LEGEND",
            bonus_type="DMGPME",
            bonus_value=10.0,
            source="M",
            condition="Tier 17, Wave 4.500"
        )
        Relic.objects.create(
            name="T:XVIII Singularity",
            rarity="LEGEND",
            bonus_type="LABSPD",
            bonus_value=10.0,
            source="M",
            condition="Tier 18, Wave 4.500"
        )

        # Tournaments
        Relic.objects.create(
            name="Copper Badge",
            rarity="RARE",
            bonus_type="DAMAGE",
            bonus_value=3.0,
            source="T",
            condition="Finish top 4 in Copper Tournament"
        )
        Relic.objects.create(
            name="Silver Badge",
            rarity="RARE",
            bonus_type="COINSB",
            bonus_value=5.0,
            source="T",
            condition="Finish top 4 in Silver Tournament"
        )
        Relic.objects.create(
            name="Gold Badge",
            rarity="EPIC",
            bonus_type="CRITFA",
            bonus_value=5.0,
            source="T",
            condition="Finish top 4 in Gold Tournament"
        )
        Relic.objects.create(
            name="Platinum Badge",
            rarity="EPIC",
            bonus_type="LABSPD",
            bonus_value=4.0,
            source="T",
            condition="Finish top 4 in Platinum Tournament"
        )
        Relic.objects.create(
            name="Champion Badge",
            rarity="LEGEND",
            bonus_type="DMGPME",
            bonus_value=10.0,
            source="T",
            condition="Finish top 4 in Champion Tournament"
        )
        Relic.objects.create(
            name="Tower Master",
            rarity="LEGEND",
            bonus_type="HEALTH",
            bonus_value=10.0,
            source="T",
            condition="Finish top 4 in Legends Tournament"
        )
        Relic.objects.create(
            name="Legend Badge",
            rarity="LEGEND",
            bonus_type="CRITFA",
            bonus_value=10.0,
            source="T",
            condition="Win the Legends Tournament"
        )

        # Others
        Relic.objects.create(
            name="1st Tower birthday",
            rarity="RARE",
            bonus_type="DAMAGE",
            bonus_value=2.0,
            source="O",
            condition="Play for 1 year"
        )
        Relic.objects.create(
            name="2nd Tower birthday",
            rarity="RARE",
            bonus_type="CRITFA",
            bonus_value=2.0,
            source="O",
            condition="Play for 2 years"
        )
        Relic.objects.create(
            name="3rd Tower birthday",
            rarity="RARE",
            bonus_type="DMGPME",
            bonus_value=2.0,
            source="O",
            condition="Play for 3 years"
        )

        # Events
        Relic.objects.create(
            name="No Spoon",
            rarity="RARE",
            bonus_type="DEFABS",
            bonus_value=2.0,
            source="E",
            condition="Matrix event; 350 medals"
        )
        Relic.objects.create(
            name="Dreamcatcher",
            rarity="RARE",
            bonus_type="COINSB",
            bonus_value=2.0,
            source="E",
            condition="Full Moon event; 350 medals"
        )
        Relic.objects.create(
            name="Bacteriophage",
            rarity="RARE",
            bonus_type="DAMAGE",
            bonus_value=2.0,
            source="E",
            condition="Viral Outbreak event; 350 medals"
        )
        Relic.objects.create(
            name="Ionized Plasma",
            rarity="RARE",
            bonus_type="DEFABS",
            bonus_value=2.0,
            source="E",
            condition="Plasma Returns event; 350 medals"
        )
        Relic.objects.create(
            name="Ancient Tome",
            rarity="RARE",
            bonus_type="LABSPD",
            bonus_value=1.5,
            source="E",
            condition="Sands of Time event; 350 medals"
        )
        Relic.objects.create(
            name="Tower Latte",
            rarity="RARE",
            bonus_type="DMGPME",
            bonus_value=2.0,
            source="E",
            condition="Autumn event; 350 medals"
        )
        Relic.objects.create(
            name="Spooky Bat",
            rarity="RARE",
            bonus_type="CRITFA",
            bonus_value=2.0,
            source="E",
            condition="Halloween event; 350 medals"
        )
        Relic.objects.create(
            name="Cherry",
            rarity="RARE",
            bonus_type="DEFABS",
            bonus_value=2.0,
            source="E",
            condition="Cherry Blossom event; 350 medals"
        )
        Relic.objects.create(
            name="Holy Joystick",
            rarity="RARE",
            bonus_type="DAMAGE",
            bonus_value=2.0,
            source="E",
            condition="Retro Arcade event; 350 medals"
        )
        Relic.objects.create(
            name="Honey Drop",
            rarity="RARE",
            bonus_type="DAMAGE",
            bonus_value=2.0,
            source="E",
            condition="Honey event; 350 medals"
        )
        Relic.objects.create(
            name="Firework",
            rarity="RARE",
            bonus_type="HEALTH",
            bonus_value=2.0,
            source="E",
            condition="New Year event; 350 medals"
        )
        Relic.objects.create(
            name="Aurora Vortex",
            rarity="RARE",
            bonus_type="HEALTH",
            bonus_value=2.0,
            source="E",
            condition="Aurora event; 350 medals"
        )
        Relic.objects.create(
            name="Dark Sight",
            rarity="RARE",
            bonus_type="DMGPME",
            bonus_value=2.0,
            source="E",
            condition="Dark Strands event; 350 medals"
        )
        Relic.objects.create(
            name="Palm Tree",
            rarity="RARE",
            bonus_type="LABSPD",
            bonus_value=2.0,
            source="E",
            condition="Retrowave event; 350 medals"
        )
        Relic.objects.create(
            name="Submarine",
            rarity="RARE",
            bonus_type="CRITFA",
            bonus_value=2.0,
            source="E",
            condition="Deep Blue Sea event; 350 medals"
        )
        Relic.objects.create(
            name="Alien Head",
            rarity="RARE",
            bonus_type="COINSB",
            bonus_value=2.0,
            source="E",
            condition="Aliens event; 350 medals"
        )
        Relic.objects.create(
            name="Warp Gate",
            rarity="RARE",
            bonus_type="COINSB",
            bonus_value=2.0,
            source="E",
            condition="Faster Than Light event; 350 medals"
        )
        Relic.objects.create(
            name="Barnacle",
            rarity="RARE",
            bonus_type="HEALTH",
            bonus_value=2.0,
            source="E",
            condition="Ocean Night event; 350 medals"
        )
        Relic.objects.create(
            name="Pizza",
            rarity="RARE",
            bonus_type="DAMAGE",
            bonus_value=2.0,
            source="E",
            condition="Invaders event; 350 medals"
        )
        Relic.objects.create(
            name="Refraction Array",
            rarity="RARE",
            bonus_type="COINSB",
            bonus_value=2.0,
            source="E",
            condition="Prismatic Lines event; 350 medals"
        )
        Relic.objects.create(
            name="Hook",
            rarity="RARE",
            bonus_type="DMGPME",
            bonus_value=2.0,
            source="E",
            condition="Sunset Fishing event; 350 medals"
        )
        Relic.objects.create(
            name="Cobweb",
            rarity="RARE",
            bonus_type="HEALTH",
            bonus_value=2.0,
            source="E",
            condition="Cobweb event; 350 medals"
        )
        Relic.objects.create(
            name="Gale Winds",
            rarity="RARE",
            bonus_type="COINSB",
            bonus_value=2.0,
            source="E",
            condition="Eye of the Storm event; 350 medals"
        )
        Relic.objects.create(
            name="Clip Ons",
            rarity="RARE",
            bonus_type="CRITFA",
            bonus_value=2.0,
            source="E",
            condition="Into the Matrix event; 350 medals"
        )
        Relic.objects.create(
            name="Rain Jacket",
            rarity="RARE",
            bonus_type="HEALTH",
            bonus_value=2.0,
            source="E",
            condition="Rainfall event; 350 medals"
        )
        Relic.objects.create(
            name="Rabies",
            rarity="RARE",
            bonus_type="LABSPD",
            bonus_value=2.0,
            source="E",
            condition="Viral Outbreak (II) event; 350 medals"
        )
        Relic.objects.create(
            name="Comet",
            rarity="RARE",
            bonus_type="DAMAGE",
            bonus_value=2.0,
            source="E",
            condition="Interstellar event; 350 medals"
        )
        Relic.objects.create(
            name="Remote Control",
            rarity="RARE",
            bonus_type="DMGPME",
            bonus_value=2.0,
            source="E",
            condition="Tower's Channel event; 350 medals"
        )
        Relic.objects.create(
            name="Anubis",
            rarity="RARE",
            bonus_type="COINSB",
            bonus_value=2.0,
            source="E",
            condition="Sands of Time (II) event; 350 medals"
        )
        Relic.objects.create(
            name="Lave Flow",
            rarity="RARE",
            bonus_type="HEALTH",
            bonus_value=2.0,
            source="E",
            condition="Volcano event; 350 medals"
        )
        Relic.objects.create(
            name="Abduction Room",
            rarity="RARE",
            bonus_type="HEALTH",
            bonus_value=2.0,
            source="E",
            condition="Abduction event; 350 medals"
        )
        Relic.objects.create(
            name="Acorn",
            rarity="RARE",
            bonus_type="DMGPME",
            bonus_value=2.0,
            source="E",
            condition="Autumn (II) event; 350 medals"
        )
        Relic.objects.create(
            name="Cauldron",
            rarity="RARE",
            bonus_type="LABSPD",
            bonus_value=2.0,
            source="E",
            condition="Halloween (II) event; 350 medals"
        )
        Relic.objects.create(
            name="Icicle",
            rarity="RARE",
            bonus_type="DAMAGE",
            bonus_value=2.0,
            source="E",
            condition="Snowstorm event; 350 medals"
        )
        Relic.objects.create(
            name="Red Pill",
            rarity="EPIC",
            bonus_type="HEALTH",
            bonus_value=5.0,
            source="E",
            condition="Matrix event; 700 medals"
        )
        Relic.objects.create(
            name="Spirit Wolf",
            rarity="EPIC",
            bonus_type="CRITFA",
            bonus_value=5.0,
            source="E",
            condition="Full Moon event; 700 medals"
        )
        Relic.objects.create(
            name="Neuron",
            rarity="EPIC",
            bonus_type="HEALTH",
            bonus_value=5.0,
            source="E",
            condition="Viral Outbreak event; 700 medals"
        )
        Relic.objects.create(
            name="Plasma Arc",
            rarity="EPIC",
            bonus_type="LABSPD",
            bonus_value=4.0,
            source="E",
            condition="Plasma Returns event; 700 medals"
        )
        Relic.objects.create(
            name="Space Sundial",
            rarity="EPIC",
            bonus_type="DAMAGE",
            bonus_value=5.0,
            source="E",
            condition="Sands of Time event; 700 medals"
        )
        Relic.objects.create(
            name="Pumpkin",
            rarity="EPIC",
            bonus_type="LABSPD",
            bonus_value=5.0,
            source="E",
            condition="Autumn event; 700 medals"
        )
        Relic.objects.create(
            name="Man Skull",
            rarity="EPIC",
            bonus_type="HEALTH",
            bonus_value=5.0,
            source="E",
            condition="Halloween event; 700 medals"
        )
        Relic.objects.create(
            name="Sakura Latern",
            rarity="EPIC",
            bonus_type="COINSB",
            bonus_value=5.0,
            source="E",
            condition="Cherry Blossom event; 700 medals"
        )
        Relic.objects.create(
            name="Controller",
            rarity="EPIC",
            bonus_type="CRITFA",
            bonus_value=5.0,
            source="E",
            condition="Retro Arcade event; 700 medals"
        )
        Relic.objects.create(
            name="Stinger",
            rarity="EPIC",
            bonus_type="CRITFA",
            bonus_value=5.0,
            source="E",
            condition="Honey event; 700 medals"
        )
        Relic.objects.create(
            name="Cheers",
            rarity="EPIC",
            bonus_type="DEFABS",
            bonus_value=5.0,
            source="E",
            condition="New Year event; 700 medals"
        )
        Relic.objects.create(
            name="Contained Ions",
            rarity="EPIC",
            bonus_type="DEFABS",
            bonus_value=5.0,
            source="E",
            condition="Aurora event; 700 medals"
        )
        Relic.objects.create(
            name="Creepy Smile",
            rarity="EPIC",
            bonus_type="DAMAGE",
            bonus_value=5.0,
            source="E",
            condition="Dark Strands event; 700 medals"
        )
        Relic.objects.create(
            name="Pixel Cube Heart",
            rarity="EPIC",
            bonus_type="HEALTH",
            bonus_value=5.0,
            source="E",
            condition="Retrowave event; 700 medals"
        )
        Relic.objects.create(
            name="The Kraken",
            rarity="EPIC",
            bonus_type="DEFABS",
            bonus_value=5.0,
            source="E",
            condition="Deep Blue Sea event; 700 medals"
        )
        Relic.objects.create(
            name="Alien Warp Drive",
            rarity="EPIC",
            bonus_type="DMGPME",
            bonus_value=5.0,
            source="E",
            condition="Aliens event; 700 medals"
        )
        Relic.objects.create(
            name="Star Ship",
            rarity="EPIC",
            bonus_type="LABSPD",
            bonus_value=4.0,
            source="E",
            condition="Faster Than Light event; 700 medals"
        )
        Relic.objects.create(
            name="Wave",
            rarity="EPIC",
            bonus_type="CRITFA",
            bonus_value=5.0,
            source="E",
            condition="Ocean Night event; 700 medals"
        )
        Relic.objects.create(
            name="Illuminati",
            rarity="EPIC",
            bonus_type="DEFABS",
            bonus_value=5.0,
            source="E",
            condition="Invaders event; 700 medals"
        )
        Relic.objects.create(
            name="Prismatic Shard",
            rarity="EPIC",
            bonus_type="DMGPME",
            bonus_value=5.0,
            source="E",
            condition="Prismatic Lines event; 700 medals"
        )
        Relic.objects.create(
            name="Fish",
            rarity="EPIC",
            bonus_type="DEFABS",
            bonus_value=5.0,
            source="E",
            condition="Sunset Fishing event; 700 medals"
        )
        Relic.objects.create(
            name="The Fly",
            rarity="EPIC",
            bonus_type="DEFABS",
            bonus_value=5.0,
            source="E",
            condition="Cobweb event; 700 medals"
        )
        Relic.objects.create(
            name="Flying House",
            rarity="EPIC",
            bonus_type="DAMAGE",
            bonus_value=5.0,
            source="E",
            condition="Eye of the Storm event; 700 medals"
        )
        Relic.objects.create(
            name="Code Stream",
            rarity="EPIC",
            bonus_type="DAMAGE",
            bonus_value=5.0,
            source="E",
            condition="Into the Matrix event; 700 medals"
        )
        Relic.objects.create(
            name="Storm Clouds",
            rarity="EPIC",
            bonus_type="CRITFA",
            bonus_value=5.0,
            source="E",
            condition="Rainfall event; 700 medals"
        )
        Relic.objects.create(
            name="Ebola",
            rarity="EPIC",
            bonus_type="DEFABS",
            bonus_value=5.0,
            source="E",
            condition="Viral Outbreak (II) event; 700 medals"
        )
        Relic.objects.create(
            name="Planetary Rings",
            rarity="EPIC",
            bonus_type="CRITFA",
            bonus_value=5.0,
            source="E",
            condition="Interstellar event; 700 medals"
        )
        Relic.objects.create(
            name="Cathode Ray Tube",
            rarity="EPIC",
            bonus_type="COINSB",
            bonus_value=5.0,
            source="E",
            condition="Tower's Channel event; 700 medals"
        )
        Relic.objects.create(
            name="Sphinx",
            rarity="EPIC",
            bonus_type="DAMAGE",
            bonus_value=5.0,
            source="E",
            condition="Sands of Time (II) event; 700 medals"
        )
        Relic.objects.create(
            name="Ash Cloud",
            rarity="EPIC",
            bonus_type="DEFABS",
            bonus_value=5.0,
            source="E",
            condition="Volcano event; 700 medals"
        )
        Relic.objects.create(
            name="Crop Circle",
            rarity="EPIC",
            bonus_type="CRITFA",
            bonus_value=5.0,
            source="E",
            condition="Abduction event; 700 medals"
        )
        Relic.objects.create(
            name="Scarf",
            rarity="EPIC",
            bonus_type="DEFABS",
            bonus_value=5.0,
            source="E",
            condition="Autumn (II) event; 700 medals"
        )
        Relic.objects.create(
            name="Witch Hat",
            rarity="EPIC",
            bonus_type="DAMAGE",
            bonus_value=5.0,
            source="E",
            condition="Halloween (II) event; 700 medals"
        )
        Relic.objects.create(
            name="Sleigh Bell",
            rarity="EPIC",
            bonus_type="HEALTH",
            bonus_value=5.0,
            source="E",
            condition="Snowstorm event; 700 medals"
        )

    def reverse(apps, schema_editor):
        pass

    operations = [
        migrations.AlterField(
            model_name='relic',
            name='name',
            field=models.CharField(help_text='Name of the Relic', max_length=200, unique=True, verbose_name='Name'),
        ),
        migrations.RunPython(init_relics, reverse),
    ]


