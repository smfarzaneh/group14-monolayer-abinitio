import numpy as np
import os

class Efield():

    @classmethod    
    def write_values(self, e_start=0.001, e_stop=0.100, steps=100, prefix='graphene'):
        relpath = '../in/' + prefix + '-efield.val'
        e_vals = np.linspace(e_start, e_stop, num=steps, endpoint=True) 
        current = os.path.dirname(__file__)
        abspath = os.path.join(current, relpath)
        if os.path.isfile(abspath):
            f = open(abspath, "w")
        else:
            f = open(abspath, "x")
        f.write("#!/bin/sh\ne_vals=( ")
        for i in range(steps):
            s = "{0:.8f}".format(e_vals[i]) + " "
            f.write(s)
        f.write(" )")
        f.close()