# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

"""Provide game-related constants for the app."""


# Python imports
from enum import Enum

# Django imports
from django.db.models import IntegerChoices, TextChoices
from django.utils.translation import gettext_lazy as _


class TowerTiers(Enum):
    """The game's different difficulty levels.

    All of them should be covered with this enum. Other code in this app will
    rely on this ``Enum`` for reference.
    """

    T1 = ("T1", _("Tier 1"))
    T2 = ("T2", _("Tier 2"))
    T3 = ("T3", _("Tier 3"))
    T4 = ("T4", _("Tier 4"))
    T5 = ("T5", _("Tier 5"))
    T6 = ("T6", _("Tier 6"))
    T7 = ("T7", _("Tier 7"))
    T8 = ("T8", _("Tier 8"))
    T9 = ("T9", _("Tier 9"))
    T10 = ("T10", _("Tier 10"))
    T11 = ("T11", _("Tier 11"))
    T12 = ("T12", _("Tier 12"))
    T13 = ("T13", _("Tier 13"))
    T14 = ("T14", _("Tier 14"))
    T15 = ("T15", _("Tier 15"))
    T16 = ("T16", _("Tier 16"))
    T17 = ("T17", _("Tier 17"))
    T18 = ("T18", _("Tier 18"))


class TowerRarities(Enum):
    """The game applies different *rarities* to different item.

    All of them should be covered with this enum. Other code in this app will
    rely on this ``Enum`` for reference.
    """

    COMMON = ("COMMON", _("Common"))
    RARE = ("RARE", _("Rare"))
    RARE_1 = ("RARE_1", _("Rare+"))
    EPIC = ("EPIC", _("Epic"))
    EPIC_1 = ("EPIC_1", _("Epic+"))
    LEGEND = ("LEGEND", _("Legendary"))
    LEGE_1 = ("LEGE_1", _("Legendary+"))
    MYTHIC = ("MYTHIC", _("Mythic"))
    MYTH_1 = ("MYTH_1", _("Mythic+"))
    ANCEST = ("ANCEST", _("Ancestral"))
    ANCE_1 = ("ANCE_1", _("Ancestral 1 star"))
    ANCE_2 = ("ANCE_2", _("Ancestral 2 star"))
    ANCE_3 = ("ANCE_3", _("Ancestral 3 star"))
    ANCE_4 = ("ANCE_4", _("Ancestral 4 star"))
    ANCE_5 = ("ANCE_5", _("Ancestral 5 star"))


class TowerWorkshopItems(Enum):
    """The game's so-called *workshop* consists of three tabs with different items.

    All of the should be covered with this enum. Other code in this app will
    rely on this ``Enum`` for reference.
    """

    # Damage tab
    DAMAGE = ("DAMAGE", _("Damage"))
    ATKSPD = ("ATKSPD", _("Attack Speed"))
    CRITCH = ("CRITCH", _("Critical Chance"))
    CRITFA = ("CRITFA", _("Critical Factor"))
    RANGE = ("RANGE", _("Range"))
    DMGPME = ("DMGPME", _("Damage/Meter"))
    MULTCH = ("MULTCH", _("Multishot Chance"))
    MULTTA = ("MULTTA", _("Multishot Targets"))
    RFCHAN = ("RFCHAN", _("Rapid Fire Chance"))
    RFDURA = ("RFDURA", _("Rapid Fire Duration"))
    BSCHAN = ("BSCHAN", _("Bounce Shot Chance"))
    BSTARG = ("BSTARG", _("Bounce Shot Targets"))
    BSRANG = ("BSRANG", _("Bounce Shot Range"))
    SCRITC = ("SCRITC", _("Super Crit Chance"))
    SCRITM = ("SCRITM", _("Super Crit Mult"))
    RENDCH = ("RENDCH", _("Rend Armor Chance"))
    RENDMU = ("RENDMU", _("Rend Armor Mult"))

    # Defense tab
    HEALTH = ("HEALTH", _("Health"))
    HREGEN = ("HREGEN", _("Health Regen"))
    DEFPER = ("DEFPER", _("Defense Percent"))
    DEFABS = ("DEFABS", _("Defense Absolute"))
    THORNS = ("THORNS", _("Thorns"))
    LIFEST = ("LIFEST", _("Lifesteal"))
    KBCHAN = ("KBCHAN", _("Knockback Chance"))
    KBFORC = ("KBFORC", _("Knockback Force"))
    ORBSPD = ("ORBSPD", _("Orb Speed"))
    ORBCNT = ("ORBCNT", _("Orbs"))
    SWSIZE = ("SWSIZE", _("Shockwave Size"))
    SWFREQ = ("SWFREQ", _("Shockwave Frequency"))
    WLMDMG = ("WLMDMG", _("Land Mine Damage"))
    WLMCHA = ("WLMCHA", _("Land Mine Chance"))
    WLMRAD = ("WLMRAD", _("Land Mine Radius"))
    DEATHD = ("DEATHD", _("Death Defy"))
    WALLHE = ("WALLHE", _("Wall Health"))
    WALLRE = ("WALLRE", _("Wall Rebuild"))

    # Utility tab
    CASHBO = ("CASHBO", _("Cash Bonus"))
    CASHWA = ("CASHWA", _("Cash/Wave"))
    COINSB = ("COINSB", _("Coins/Kill Bonus"))
    COINSW = ("COINSW", _("Coins/Wave"))
    FATKUP = ("FATKUP", _("Free Attack Upgrade"))
    FDEFUP = ("FDEFUP", _("Free Defense Upgrade"))
    FUTIUP = ("FUTIUP", _("Free Utility Upgrade"))
    INTERE = ("INTERE", _("Interest/Wave"))
    RECOAM = ("RECOAM", _("Recovery Amount"))
    RECOMA = ("RECOMA", _("Max Recovery"))
    RECOCH = ("RECOCH", _("Package Chance"))
    EALSKP = ("EALSKP", _("Enemy Attack Level Skip"))
    EHLSKP = ("EHLSKP", _("Enemy Health Level Skip"))


class RunTiers(TextChoices):
    """The actual TextChoices to be used in Django code.

    The actual reference is :class:`penthouse.game_constants.TowerTiers`.
    """

    T1 = TowerTiers.T1.value
    T2 = TowerTiers.T2.value
    T3 = TowerTiers.T3.value
    T4 = TowerTiers.T4.value
    T5 = TowerTiers.T5.value
    T6 = TowerTiers.T6.value
    T7 = TowerTiers.T7.value
    T8 = TowerTiers.T8.value
    T9 = TowerTiers.T9.value
    T10 = TowerTiers.T10.value
    T11 = TowerTiers.T11.value
    T12 = TowerTiers.T12.value
    T13 = TowerTiers.T13.value
    T14 = TowerTiers.T14.value
    T15 = TowerTiers.T15.value
    T16 = TowerTiers.T16.value
    T17 = TowerTiers.T17.value
    T18 = TowerTiers.T18.value


class RelicBonusType(TextChoices):
    """The game's relics modify/increase certain stats of the tower."""

    DAMAGE = TowerWorkshopItems.DAMAGE.value
    CRITFA = TowerWorkshopItems.CRITFA.value
    COINSB = TowerWorkshopItems.COINSB.value
    LABSPD = "LABSPD", _("Lab Speed")
    DEFABS = TowerWorkshopItems.DEFABS.value
    DMGPME = TowerWorkshopItems.DMGPME.value
    HEALTH = TowerWorkshopItems.HEALTH.value
    ATKSPD = TowerWorkshopItems.ATKSPD.value
    CRITCH = TowerWorkshopItems.CRITCH.value
    ULTDMG = "ULTDMG", _("Ultimate Damage")
    FATKUP = TowerWorkshopItems.FATKUP.value
    FDEFUP = TowerWorkshopItems.FDEFUP.value
    SCRITC = TowerWorkshopItems.SCRITC.value
    BOTRNG = "BOTRNG", _("Bot Range")


class RelicRarity(TextChoices):
    """The game's relics have given rarities."""

    RARE = TowerRarities.RARE.value
    EPIC = TowerRarities.EPIC.value
    LEGENDARY = TowerRarities.LEGEND.value


class RelicSource(TextChoices):
    """Relics can be obtained from different sources."""

    MILESTONE = ("M", _("Milestone"))
    TOURNAMENT = ("T", _("Tournament"))
    EVENT = ("E", _("Event"))
    OTHER = ("O", _("Other"))


class TowerUnitSuffix(IntegerChoices):
    """The game's suffixes for number values.

    Actually there are even more. These are pre-defined until ``O``, which
    should be enough for all of this app's needs.
    """

    UNIT_K = 1000, "k"
    UNIT_M = 1000000, "M"
    UNIT_B = 1000000000, "B"
    UNIT_T = 1000000000000, "T"
    UNIT_Q_MIN = 1000000000000000, "q"
    UNIT_Q = 1000000000000000000, "Q"
    UNIT_S_MIN = 1000000000000000000000, "s"
    UNIT_S = 1000000000000000000000000, "S"
    UNIT_O = 1000000000000000000000000000, "O"


class TowerUnits(Enum):
    """The game's units.

    These are standard american names for large numbers. See
    https://en.wikipedia.org/wiki/Names_of_large_numbers for reference.
    """

    nonillion = 30, "N"
    octillion = 27, "O"
    septillion = 24, "S"
    sextillion = 21, "s"
    quintillion = 18, "Q"
    quadrillion = 15, "q"
    trillion = 12, "T"
    billion = 9, "B"
    million = 6, "M"
    kilo = 3, "k"

    @classmethod
    def get_multiplier_prefix(cls):
        """Return a dict with the abbreviation as key and the exponents as value."""
        return {i.value[1]: i.value[0] for i in cls}
