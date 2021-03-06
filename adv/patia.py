import adv_test
from adv import *
from module.bleed import Bleed
from slot.a import *

def module():
    return Patia

class Patia(Adv):
    a1 = ('bt',0.25)

    def prerun(this):
        this.bleed = Bleed("g_bleed",0).reset()
        this.a3_iscding = 0

    def s1_proc(this, e):
        Event('defchain')()
        #Teambuff('db_test',0.08,15).on()

    def s2_proc(this, e):
        if random.random() < 0.8:
            Bleed("s2_bleed", 0.99).on()

    def a3_cooldown(this, t):
        this.a3_iscding = 0
        log('cd','a3','end')

    def a3_act(this):
        #logcat()
        #print this.a3_iscding
        #exit()
        if not this.a3_iscding :
            this.a3_iscding = 1
            Timer(this.a3_cooldown).on(15)
            log('cd','a3','start')
            Selfbuff('a3',0.05,5,'crit','chance').on()
        else:
            log('cd','a3','trigger failed')

    def charge(this, name, sp):
        if this.s1.check():
            return Adv.charge(this, name, sp)
        r = Adv.charge(this, name, sp)
        if this.s1.check():
            this.a3_act()
        return r

if __name__ == '__main__':
    conf = {}
    conf['slots.a'] = VC()+FRH()
    conf['acl'] = """
        `s1, seq=5
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2,mass=1)


