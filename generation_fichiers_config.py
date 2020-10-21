# python librairies
import numpy as np
import matplotlib.pyplot as plt
from termcolor import colored
import os

#====================================================================================

def write_init_file():
    lines = list('')
    lines.append(" 0.  0.00  0.00  0.00  0.00  0.00  0.00 	# cu0 cux cuy cv0 cvx cvy omega")
    lines.append(" 0.00					  	                # tini")
    lines.append(" 0  						                # ishear")
    lines.append(" 0						                    # iswirl")
    lines.append(" 0 1")
    lines.append("10   0                                      # nwave (nwave = 1 : init taux suivant le maillage cad selon le numero de cellule plutot que les distances), nwaveout")
    lines.append("1                                           # nombre de carres ou cubes a initialiser (mettre 1 pour initialiser le 2nd fluide sir diphasique)")
    lines.append("0.    0.200  0. 0.025  0.  1.   1. 0.       # xdeb, xfin, ydeb, yfin, zdeb, zfin, tauini2, tauini3")

    myfile = open(case_name+".init", "w")
    for i in range( len(lines) ):
        myfile.write( lines[i]+"\n" )
    myfile.close()


def write_phys_file():
    lines = list('')
    lines.append("    1.00E+00   1.50E-05  0.0E+00 # ro1, xmu1, xmut1  (FLUIDE = AIR a 20°C)")
    lines.append("    -1.0025E+01   0.00E+00  0.0E+00   # dpdx, dpdy, dpdz")
    lines.append("    -2.5075E-02  -9.81E+00  0.0E+00	# grx, gry, grz")

    myfile = open(case_name+".phys", "w")
    for i in range( len(lines) ):
        myfile.write( lines[i]+"\n" )
    myfile.close()

#------------------------------------------------------------------------------
#                       Serious stuff begin here
#------------------------------------------------------------------------------


case_name = "pois"
write_init_file()
write_phys_file()
