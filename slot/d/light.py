from slot import *

class Cupid(DragonBase):
    ele = 'light'
    att = 119

class Lindworm(DragonBase):
    ele = 'light'
    att = 100
    aura = [('att','passive',0.45)]

class Gilgamesh(DragonBase):
    ele = 'light'
    att = 124
    aura = [('att','passive',0.50)]

class Takemikazuchi(DragonBase):
    ele = 'light'
    att = 124
    aura = [('att','passive',0.40), ('att', 'killer', 0.25,'overdrive')]

class Unreleased_LightSkillDamage(DragonBase):
    ele = 'light'
    att = 124
    aura = [('att','passive',0.2),
            ('s','passive',0.9)]

class Corsaint_Phoenix(DragonBase):
    ele = 'light'
    att = 124
    aura = ('att','passive',0.5)

    def oninit(this, adv):
        DragonBase.oninit(this, adv)
        this.adv = adv
        m = adv.Modifier('lpp','att','killer',0)
        m.get = this.getbane

    def getbane(this):
        return this.adv.afflics.paralysis.get()*0.2
C_Phoenix = Corsaint_Phoenix

class Daikokuten(DragonBase):
    ele = 'light'
    att = 124
    aura = [('att','passive',0.55),
            ('att','passive',0.25,'hit15')]

class Shishimai(DragonBase):
    ele = 'light'
    att = 75
    aura = [('crit','damage',0.7)]

# class GalaShishimai_450CritDmg(DragonBase):
#     ele = 'light'
#     att = 124
#     aura = [('crit','damage',4.5)]
