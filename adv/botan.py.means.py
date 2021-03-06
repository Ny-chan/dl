import adv_test
from adv import botan
from module.bleed import mBleed

def module():
    return Botan

class Botan(botan.Botan):
    def prerun(this):
        this.bleed = mBleed("g_bleed",0).reset()

    def s1_proc(this, e):
        mBleed("s1_bleed", 1.32).on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, fsc
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=-2,mass=0)
