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

    @classmethod
    def write_kpoints(self, direction='x', num_k=201):
        relpath = '../in/k' + direction + '.val'
        current = os.path.dirname(__file__)
        abspath = os.path.join(current, relpath)
        if os.path.isfile(abspath):
            f = open(abspath, "w")
        else:
            f = open(abspath, "x")
        f.write("#!/bin/sh\nk_string=\"")
        K_point_x = 2.0/3.0
        k_vals = np.linspace(-0.5, 0.5, num_k, endpoint=True)        
        f.write(str(num_k) + "\n")
        for k in k_vals:
            if direction=='x':
                s = " {0:.8f}  {1:.8f}  {2:.8f}  1.0\n".format(k + K_point_x, 0.0, 0.0)
            else:
                s = " {0:.8f}  {1:.8f}  {2:.8f}  1.0\n".format(K_point_x, k, 0.0)
            f.write(s)
        f.write("\"")
        f.close()