import discord
from discord.ext import commands
from discord import Embed

class embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    allspells = [Embed(title='All Spells - Cantrips (pg.1)', color=discord.Color.green(), description='Blade Ward\n\nDancing Lights\n\nFriends\n\nLight\n\nMage Hand\n\nMending\n\nMessage\n\nMinor Illusion\n\nPrestidigitation\n\nThunderclap\n\nTrue Strike\n\nVicious Mockery'),
    Embed(title='All Spells - Cantrips (pg.2)', color=discord.Color.green(), description='Guidance\n\nResistance\n\nSacred Flame\n\nThaumaturgy\n\nDruidcraft\n\nPoison Spray\n\nProduce Flame\n\nShillelagh'),
    Embed(title='All Spells - Cantrips (pg.3)', color=discord.Color.green(), description='Bless\n\nCommand\n\nCure Wounds\n\nDetect Evil and Good\n\nDetect Magic\n\nDetect Poison and Disease\n\nDivine Favor'),
    Embed(title='All Spells - Cantrips (pg.4)', color=discord.Color.green(), description='Heroism\n\nProtection from Evil and Good\n\nPurify Food and Drink\n\nShield of Faith\n\nAlarm\n\nAnimal friendship\n\nFog Cloud'),
    Embed(title='All Spells - Cantrips (pg.5)', color=discord.Color.green(), description='Goodberry\n\nHunter\'s Mark\n\nJump\n\nLongstrider\n\nSpeak with Animals\n\nAcid Splash\n\nChill Touch\n\nFire Bolt\n\nRay of Frost'),
    Embed(title='All Spells - Cantrips (pg.6)', color=discord.Color.green(), description='Shocking Grasp\n\nTrue Strike\n\nEldritch Blast'),
    Embed(title='All Spells - 1st level (pg.1)', color=discord.Color.green(), description='Animal Friendship\n\nBane\n\nCharm Person\n\nComprehend Languages\n\nCure Wounds\n\nDetect Magic\n\nDisguise Self\n\nDissonant Whispers'),
    Embed(title='All Spells - 1st level (pg.2)', color=discord.Color.green(), description='Earth Tremor\n\nFaerie Fire\n\nFeather Fall\n\nHealing Word\n\nHeroism\n\nHideous Laughter\n\nIdentify\n\nIllusory Script\n\nLongstrider'),
    Embed(title='All Spells - 1st level (pg.3)', color=discord.Color.green(), description='Silent Image\n\nSleep\n\nSpeak with Animals\n\nThunderwave\n\nUnseen Servant\n\nBless\n\nCommand\n\nCreate or Destroy Water\n\nDetect Evil and Good'),
    Embed(title='All Spells - 1st level (pg.4)', color=discord.Color.green(), description='Detect Poison and Disease\n\nGuiding Bolt\n\nInflict Wounds\n\nProtetion from Evil and Good\n\nPurify Food and Drink\n\nSanctuary\n\nShield of Faith\n\nEntangle\n\nFog Cloud'),
    Embed(title='All Spells - 1st level (pg.5)', color=discord.Color.green(), description='Goodberry\n\nJump\n\nAid\n\nBranding Smite\n\nFind Steed\n\nLesser Restoration\n\nLocate Object\n\nMagic Weapon\n\nProtection from Poison\n\nZone of Truth'),
    Embed(title='All Spells - 1st level (pg.6)', color=discord.Color.green(), description='Alarm\n\nHunter\'s mark\n\nAcid Splash\n\nChill Touch\n\nDancing Lights\n\nFire Bolt\n\nMage Hand\n\nMending\n\nMessage\n\nMinor Illusion'),
    Embed(title='All Spells - 1st level (pg.7)', color=discord.Color.green(), description='Poison Spray\n\nPrestidigitation\n\nRay of Frost\n\nShocking Grasp\n\nTrue Strike\n\nEldritch Blast')]



    races = [Embed(title="Dragonborn", color=discord.Color.green(), description="d!race dragonborn"),
    Embed(title="Dwarf", color=discord.Color.green(), description="d!race dwarf"),
    Embed(title='Elf', color=discord.Color.green(), description="d!race elf"),
    Embed(title='Gnome', color=discord.Color.green(), description="d!race gnome"),
    Embed(title='Half-Elf', color=discord.Color.green(), description="d!race half-elf"),
    Embed(title='Halfling', color=discord.Color.green(), description="d!race halfling"),
    Embed(title='Half-Orc', color=discord.Color.green(), description="d!race half-orc"),
    Embed(title='Human', color=discord.Color.green(), description="d!race human"),
    Embed(title='Tiefling', color=discord.Color.green(), description="d!race tiefling"),
    Embed(title='Leonin', color=discord.Color.green(), description="d!race leonin"),
    Embed(title='Satyr', color=discord.Color.green(), description="d!race satyr"),
    Embed(title='Aarakocra', color=discord.Color.green(), description="d!race aarakocra"),
    Embed(title='Genasi', color=discord.Color.green(), description="d!race genasi"),
    Embed(title='Goliath', color=discord.Color.green(), description="d!race goliath"),
    Embed(title='Aasimar', color=discord.Color.green(), description="d!race aasimar"),
    Embed(title='Bugbear', color=discord.Color.green(), description="d!race bugbear"),
    Embed(title='Firbolg', color=discord.Color.green(), description="d!race firbolg"),
    Embed(title='Goblin', color=discord.Color.green(), description="d!race goblin"),
    Embed(title='Hobgoblin', color=discord.Color.green(), description="d!race hobgoblin"),
    Embed(title='Kenku', color=discord.Color.green(), description="d!race kenku"),
    Embed(title='Kobold', color=discord.Color.green(), description="d!race kobold"),
    Embed(title='Lizardfolk', color=discord.Color.green(), description="d!race lizardfolk"),
    Embed(title='Orc', color=discord.Color.green(), description="d!race orc"),
    Embed(title='Tabaxi', color=discord.Color.green(), description="d!race tabaxi"),
    Embed(title='Triton', color=discord.Color.green(), description="d!race triton"),
    Embed(title='Yuan-ti Pureblood', color=discord.Color.green(), description="d!race yuan-ti pureblood"),
    Embed(title='Changeling', color=discord.Color.green(), description="d!race changeling"),
    Embed(title='Kalashtar', color=discord.Color.green(), description="d!race kalashtar"),
    Embed(title='Shifter', color=discord.Color.green(), description="d!race shifter"),
    Embed(title='Warforged', color=discord.Color.green(), description="d!race warforged"),
    Embed(title='Gith', color=discord.Color.green(), description="d!race gith"),
    Embed(title='Centaur', color=discord.Color.green(), description="d!race centaur"),
    Embed(title='Loxodon', color=discord.Color.green(), description="d!race loxodon"),
    Embed(title='Minotaur', color=discord.Color.green(), description="d!race minotaur"),
    Embed(title='Simic Hybrid', color=discord.Color.green(), description="d!race simic hybrid"),
    Embed(title='Vedalken', color=discord.Color.green(), description="d!race vedalken"),
    Embed(title='Verdan', color=discord.Color.green(), description="d!race verdan")]

    classes = [Embed(title='Barbarian', color=discord.Color.green(), description='d!class barbarian'),
    Embed(title='Bard', color=discord.Color.green(), description='d!class bard'),
    Embed(title='Cleric', color=discord.Color.green(), description='d!class cleric'),
    Embed(title='Druid', color=discord.Color.green(), description='d!class druid'),
    Embed(title='Fighter', color=discord.Color.green(), description='d!class fighter'),
    Embed(title='Monk', color=discord.Color.green(), description='d!class monk'),
    Embed(title='Paladin', color=discord.Color.green(), description='d!class paladin'),
    Embed(title='Ranger', color=discord.Color.green(), description='d!class ranger'),
    Embed(title='Rogue', color=discord.Color.green(), description='d!class rogue'),
    Embed(title='Sorcerer', color=discord.Color.green(), description='d!class sorcerer'),
    Embed(title='Warlock', color=discord.Color.green(), description='d!class warlock'),
    Embed(title='Wizard', color=discord.Color.green(), description='d!class wizard'),
    Embed(title='Artificer', color=discord.Color.green(), description='d!class artificer')]

def setup(bot):
    bot.add_cog(embeds(bot))
