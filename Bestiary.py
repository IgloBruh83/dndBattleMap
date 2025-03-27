from Modules.Unit import Unit
from random import randint
from Modules.Misc import Roll


class Goblin (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/Goblin_Unit.png', 'UnitGraphics/Goblin_Icon.png', scale[0], scale[1])
        self.devScale = 0.25
        self.name = 'Goblin'
        self.team = 'Enemy'
        self.maxhp = Roll('2d6+3'); self.hp = self.maxhp
        self.sb = { 'STR': 8, 'DEX': 14, 'CON': 10, 'INT': 10, 'WIS': 8, 'CHA': 8 }
        self.armorClass = 13
        self.moveset = [
            "Melee attack: +4 | 1d6+2 slashing",
            "Ranged attack: +4 | 1d6+2 piercing",
            "Nimble escape: bonus action"
        ]
        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()


class JungleGoblin (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/JungleGoblin_Unit.png', 'UnitGraphics/JungleGoblin_Icon.png', scale[0], scale[1])
        self.devScale = 0.25
        self.name = 'Jungle Goblin'
        self.team = 'Enemy'
        self.maxhp = Roll('3d6+3'); self.hp = self.maxhp
        self.sb = { 'STR': 8, 'DEX': 16, 'CON': 10, 'INT': 11, 'WIS': 10, 'CHA': 7 }
        self.armorClass = 14
        self.moveset = [
            "Melee attack: +5 | 1d6+3 slashing",
            "Ranged attack: +3 | 1d4 piercing + 2d4 poison",
            "Nimble escape: bonus action"
        ]
        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()


class EliteGoblin (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/EliteGoblin_Unit.png', 'UnitGraphics/EliteGoblin_Icon.png', scale[0], scale[1])
        self.devScale = 0.25
        self.name = 'Elite Goblin'
        self.team = 'Enemy'
        self.maxhp = Roll('6d6+5'); self.hp = self.maxhp
        self.sb = { 'STR': 10, 'DEX': 14, 'CON': 10, 'INT': 10, 'WIS': 8, 'CHA': 10 }
        self.armorClass = 15
        self.moveset = [
            "Melee attack: +4 | 1d6+3 slashing",
            "Multiattack: second attack with disadvantage",
            "Nimble escape: bonus action",
            "Redirect attack: reaction"
        ]
        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()


class Bandit (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/Bandit_Unit.png', 'UnitGraphics/Bandit_Icon.png', scale[0], scale[1])
        self.devScale = 0.15
        self.name = 'Bandit'
        self.team = 'Enemy'
        self.maxhp = Roll('3d8+3'); self.hp = self.maxhp
        self.sb = { 'STR': 11, 'DEX': 14, 'CON': 12, 'INT': 10, 'WIS': 10, 'CHA': 10 }
        self.armorClass = 14
        self.moveset = [
            "Melee attack: +4 | 1d6+2 slashing",
            "Ranged attack: +4 | 1d8+2 piercing"
        ]
        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()


class BanditMage (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/BanditMage_Unit.png', 'UnitGraphics/BanditMage_Icon.png', scale[0], scale[1])
        self.devScale = 0.35
        self.name = 'Bandit Mage'
        self.team = 'Enemy'
        self.maxhp = Roll('3d6+3'); self.hp = self.maxhp
        self.sb = { 'STR': 8, 'DEX': 14, 'CON': 12, 'INT': 15, 'WIS': 10, 'CHA': 10 }
        self.armorClass = 12
        self.moveset = [
            "Magic usage: 1[4], 2[2]"
        ]
        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()


class Skeleton (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/Skeleton_Unit.png', 'UnitGraphics/Skeleton_Icon.png', scale[0], scale[1])
        self.devScale = 0.25
        self.name = 'Skeleton'
        self.team = 'Enemy'
        self.maxhp = Roll('2d8+4'); self.hp = self.maxhp
        self.sb = { 'STR': 10, 'DEX': 14, 'CON': 15, 'INT': 6, 'WIS': 8, 'CHA': 5 }
        self.armorClass = 13
        self.moveset = [
            "Melee attack: +4 | 1d6+2 piercing",
            "Ranged attack: +4 | 1d6+2 piercing",
            "Vuln: Bludgeoning | Immun: Poison"
        ]
        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()


class Kobold (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/Kobold_Unit.png', 'UnitGraphics/Kobold_Icon.png', scale[0], scale[1])
        self.devScale = 0.25
        self.name = 'Kobold'
        self.team = 'Enemy'
        self.maxhp = Roll('3d6+2'); self.hp = self.maxhp
        self.sb = { 'STR': 7, 'DEX': 15, 'CON': 9, 'INT': 8, 'WIS': 7, 'CHA': 8 }
        self.armorClass = 12
        self.moveset = [
            "Melee attack: +4 | 1d4+2 piercing",
            "Pack tactics: passive"
        ]
        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()


class Boar (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/Boar_Unit.png', 'UnitGraphics/Boar_Icon.png', scale[0], scale[1])
        self.devScale = 0.20
        self.name = 'Boar'
        self.team = 'Neutral'
        self.maxhp = Roll('2d8+2'); self.hp = self.maxhp
        self.sb = { 'STR': 13, 'DEX': 11, 'CON': 12, 'INT': 2, 'WIS': 9, 'CHA': 5 }
        self.armorClass = 11
        self.moveset = [
            "Melee attack: +3 | 1d6+1 slashing",
            "Charge: +1d6 slashing | STR 11 or prone"
        ]
        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()


class Wolf (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/Wolf_Unit.png', 'UnitGraphics/Wolf_Icon.png', scale[0], scale[1])
        self.devScale = 0.15
        self.name = 'Wolf'
        self.team = 'Neutral'
        self.maxhp = Roll('3d8+2'); self.hp = self.maxhp
        self.sb = { 'STR': 11, 'DEX': 15, 'CON': 13, 'INT': 6, 'WIS': 7, 'CHA': 3 }
        self.armorClass = 14
        self.moveset = [
            "Melee attack: +4 | 1d6+1 slashing",
            "Bloodletting: CON 12 | Bleeding",
            "Single mind: 2/per fight | Pass turn",
            "Pack tactics: passive"
        ]
        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()


class Paladin (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/Paladin_Unit.png', 'UnitGraphics/Paladin_Icon.png', scale[0], scale[1])
        self.devScale = 0.3
        self.name = 'Paladin'
        self.team = 'Neutral'
        self.maxhp = Roll('5d10+5'); self.hp = self.maxhp
        self.sb = { 'STR': 16, 'DEX': 10, 'CON': 14, 'INT': 11, 'WIS': 12, 'CHA': 16 }
        self.armorClass = 18
        self.moveset = [
            "Melee attack: +6 | 1d10+4 slashing",
            "Smite: +2d8 radiant | +3d8 radiant",
            "Lay on Hands: 12/25 heal 4/2 per day",
            "Holy shield: +2 AC, bonus action"
        ]
        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()


class Shadow (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/Shadow_Unit.png', 'UnitGraphics/Shadow_Icon.png', scale[0], scale[1])
        self.devScale = 0.22
        self.name = 'Shadow'
        self.team = 'Enemy'
        self.maxhp = Roll('6d8'); self.hp = self.maxhp
        self.sb = { 'STR': 8, 'DEX': 16, 'CON': 10, 'INT': 6, 'WIS': 12, 'CHA': 10 }
        self.armorClass = 14
        self.moveset = [
            "Shadow claws: +5 | 2d6+2 necrotic",
            "Siphoning: CON 12 | Steal 2d6 max hp",
            "Shadow step: bonus action",
            "Vuln: Radiant | Res: Physical"
        ]
        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()


class ReaperShadow (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/DeathShadow_Unit.png', 'UnitGraphics/DeathShadow_Icon.png', scale[0], scale[1])
        self.devScale = 0.36
        self.name = 'Reaper Shadow'
        self.team = 'Enemy'
        self.maxhp = Roll('15d10+30'); self.hp = self.maxhp
        self.sb = { 'STR': 14, 'DEX': 18, 'CON': 14, 'INT': 8, 'WIS': 14, 'CHA': 16 }
        self.armorClass = 17
        self.moveset = [
            "Shadow claws: +6 | 3d6+2 necrotic",
            "Presence: WIS 6 | AOE Fear | Bonus act.",
            "Immune to ALL dmg. in darkness",
            "Vuln: Radiant | Res: Physical"
        ]
        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()


class Guard (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/Guard_Unit.png', 'UnitGraphics/Guard_Icon.png', scale[0], scale[1])
        self.devScale = 0.22
        self.name = 'Guard'
        self.team = 'Neutral'
        self.maxhp = Roll('5d10+5'); self.hp = self.maxhp
        self.sb = { 'STR': 14, 'DEX': 14, 'CON': 14, 'INT': 10, 'WIS': 9, 'CHA': 11 }
        self.armorClass = 16
        self.moveset = [
            "Melee attack: +4 | 1d10+2 piercing",
            "Ranged attack: +4 | 1d8+2 piercing"
        ]
        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()





# PLAYERS ------------------------------------------------------------

class Mzhuka (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/PLAYER1.png', 'UnitGraphics/PLAYER1.png', scale[0], scale[1])
        self.devScale = 0.35
        self.name = 'Mzhuka'
        self.team = 'Party'
        self.maxhp = 27; self.hp = self.maxhp
        self.sb = { 'STR': 8, 'DEX': 14, 'CON': 12, 'INT': 16, 'WIS': 14, 'CHA': 7 }
        self.armorClass = 17

        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()

class Glurp (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/PLAYER2.png', 'UnitGraphics/PLAYER2.png', scale[0], scale[1])
        self.devScale = 0.35
        self.name = 'Glurp'
        self.team = 'Party'
        self.maxhp = 30; self.hp = self.maxhp
        self.sb = {'STR': 8, 'DEX': 18, 'CON': 14, 'INT': 7, 'WIS': 14, 'CHA': 10}
        self.armorClass = 15

        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX'] // 2 - 5 + self.initBonus
        self.RenderUnit()

class Ustalost (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/PLAYER3.png', 'UnitGraphics/PLAYER3.png', scale[0], scale[1])
        self.devScale = 0.35
        self.name = 'Ustalost'
        self.team = 'Party'
        self.maxhp = 27; self.hp = self.maxhp
        self.sb = { 'STR': 6, 'DEX': 14, 'CON': 16, 'INT': 14, 'WIS': 14, 'CHA': 18 }
        self.armorClass = 14

        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX']//2-5 + self.initBonus
        self.RenderUnit()

class Valyana (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/PLAYER4.png', 'UnitGraphics/PLAYER4.png', scale[0], scale[1])
        self.devScale = 0.35
        self.name = 'Valyana'
        self.team = 'Party'
        self.maxhp = 20; self.hp = self.maxhp
        self.sb = {'STR': 12, 'DEX': 12, 'CON': 12, 'INT': 13, 'WIS': 18, 'CHA': 18}
        self.armorClass = 11

        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX'] // 2 - 5 + self.initBonus
        self.RenderUnit()

class Nacho (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/Nacho_Unit.png', 'UnitGraphics/Nacho_Icon.png', scale[0], scale[1])
        self.devScale = 0.35
        self.name = 'Mr. Nacho'
        self.team = 'Party'
        self.maxhp = 32; self.hp = self.maxhp
        self.sb = {'STR': 6, 'DEX': 16, 'CON': 11, 'INT': 17, 'WIS': 11, 'CHA': 12}
        self.armorClass = 16

        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX'] // 2 - 5 + self.initBonus
        self.RenderUnit()






# BOSSES ------------------------------------------------------------

class LetMeSoloHer (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/LetMeSoloHer_Unit.png', 'UnitGraphics/LetMeSoloHer_Icon.png', scale[0], scale[1])
        self.devScale = 0.75
        self.name = 'Let Me Solo Her'
        self.maxhp = 10; self.hp = self.maxhp
        self.sb = {'STR': 9, 'DEX': 182, 'CON': 5 , 'INT': 13, 'WIS': 12, 'CHA': 7}
        self.armorClass = 96

        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX'] // 2 - 5 + self.initBonus
        self.RenderUnit()

class SoulDemon (Unit):
    def __init__(self, canvas, scale):
        super().__init__(canvas, 'UnitGraphics/SoulDemon_Unit.png', 'UnitGraphics/SoulDemon_Icon.png', scale[0], scale[1])
        self.devScale = 0.75
        self.name = 'Soul Demon'
        self.maxhp = 250; self.hp = self.maxhp
        self.sb = {'STR': 14, 'DEX': 24, 'CON': 14 , 'INT': 16, 'WIS': 13, 'CHA': 7}
        self.armorClass = 19

        # Automatic part
        self.initiative = randint(1, 20) + self.sb['DEX'] // 2 - 5 + self.initBonus
        self.RenderUnit()
