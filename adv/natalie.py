import adv_test
import adv
from adv import *
from module import energy
from slot.a import *
from slot.d import *
import random

def module():
    return Natalie


class Natalie(adv.Adv):
    conf = {}
    conf['slot.a'] = HoH() + JotS()
    conf['slot.d'] = Shinobi()
     
    def pre(this):
        random.seed()
        this.crisis = 0
        if this.condition('energy'):
            this.init = this.c_init
        if this.condition('keep hp20 after first s2'):
            this.crisis = -1

    def init(this):
        this.energy = energy.Energy(this,
                self={} ,
                team={} 
                )

    def c_init(this):
        this.energy = energy.Energy(this,
                self={'s1':1,'a1':1} ,
                team={}
                )
        this.a3atk = Selfbuff('a3atk',0.20,-1,'att','passive').on()
        this.a3spd = Selfbuff('a3spd',0.10,-1,'spd').on()


    def s1_proc(this, e):
        if this.crisis > 0:
            this.dmg_make('o_s1_crisis', this.crisis*10.84)
        if random.random() < 0.8:
            this.energy.add_energy('a1')

    def s2_proc(this, e):
        if this.crisis == -1:
            this.crisis = 1*0.8*0.8
        else:
            Selfbuff('s2str',0.15,10).on()





if __name__ == '__main__':
    #conf = {}
    #conf['acl'] = """
    #    `s1, this.energy() < 5
    #    `s3, seq=5 and this.energy() = 5
    #    """

    conf = {}
    conf['acl'] = """
        `s2
        `s1
        `s3, seq=5
        """

    adv_test.test(module(), conf, verbose=-2, mass=1)

