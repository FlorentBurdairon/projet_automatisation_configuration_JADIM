# python librairies
import numpy as np
import matplotlib.pyplot as plt
from termcolor import colored
import os

#====================================================================================

def dictionaries():
    # .init
    init_dict = {"cu0": 0., "cux": 0., "cuy": 0., "cv0": 0., "cvx": 0., "cvy": 0., "omega": 0., "tini": 0., "ishear": 0, "iswirl": 0}
    init_dict["nwave"] = 10
    init_dict["nwaveout"] = 0
    init_dict["nblock"] = 1
    init_dict["xdeb"] = 0.0
    init_dict["xfin"] = 200e-3
    init_dict["ydeb"] = 0.0
    init_dict["yfin"] = 25e-3
    init_dict["zdeb"] = 0.0
    init_dict["zfin"] = 1.0
    init_dict["tauini2"] = 1.0
    init_dict["tauini3"] = 0.0

    # .phys
    phys_dict = dict()
    phys_dict["ro1"] = 1.00e+0
    phys_dict["xmu1"] = 1.50e-5
    phys_dict["xmut1"] = 0.0E+00
    phys_dict["dpdx"] = -1.0025E+01
    phys_dict["dpdy"] = 0.0E+00
    phys_dict["dpdz"] = 0.0E+00
    phys_dict["grx"] = -2.5075E-02
    phys_dict["gry"] = -9.81E+00
    phys_dict["grz"] = 0.0E+00

    return init_dict, phys_dict

def write_init_file():
    myfilename = case_name + ".init"
    myfile = open( dirname + myfilename, "w")

    #for item in init_dict.items():
    #    print(f"{item[0]} = {item[1]}")
    mystring = f"{init_dict['cu0']}\t{init_dict['cux']}\t{init_dict['cuy']}\t{init_dict['cv0']}\t{init_dict['cvx']}\t{init_dict['cvy']}\t{init_dict['omega']}"
    print(mystring)
    myfile.write( mystring+'\n' )
    mystring = f"{init_dict['tini']}\n{init_dict['ishear']}\n{init_dict['iswirl']}"
    print(mystring)
    myfile.write( mystring+'\n' )
    mystring = f"{0}" + '\t' + f"{1}"
    print(mystring)
    myfile.write( mystring+'\n' )
    mystring = f"{init_dict['nwave']}\t{init_dict['nwaveout']}"
    print(mystring)
    myfile.write( mystring+'\n' )
    mystring = f"{init_dict['nblock']}"
    print(mystring)
    myfile.write( mystring+'\n' )
    mystring = f"{init_dict['xdeb']}\t{init_dict['xfin']}\t{init_dict['ydeb']}\t{init_dict['yfin']}\t{init_dict['zdeb']}\t{init_dict['zfin']}\t{init_dict['tauini2']}\t{init_dict['tauini3']}"
    print(mystring)
    myfile.write( mystring )

    # Methode brute avec uniquement des strings
    """
    lines = list('')
    lines.append(" 0.  0.00  0.00  0.00  0.00  0.00  0.00 	# cu0 cux cuy cv0 cvx cvy omega")
    lines.append(" 0.00					  	                # tini")
    lines.append(" 0  						                # ishear")
    lines.append(" 0						                    # iswirl")
    lines.append(" 0 1")
    lines.append("10   0                                      # nwave (nwave = 1 : init taux suivant le maillage cad selon le numero de cellule plutot que les distances), nwaveout")
    lines.append("1                                           # nombre de carres ou cubes a initialiser (mettre 1 pour initialiser le 2nd fluide sir diphasique)")
    lines.append("0.    0.200  0. 0.025  0.  1.   1. 0.       # xdeb, xfin, ydeb, yfin, zdeb, zfin, tauini2, tauini3")
    for i in range( len(lines) ):
        myfile.write( lines[i]+"\n" )
    """

    myfile.close()
    print(f"File " + colored(f"{myfilename}", "yellow") + " processed")

def write_phys_file():
    myfilename = case_name + ".phys"
    myfile = open( dirname + myfilename, "w")

    #for item in init_dict.items():
    #    print(f"{item[0]} = {item[1]}")
    mystring = f"{phys_dict['ro1']:.2e}\t{phys_dict['xmu1']:.2e}\t{phys_dict['xmut1']:.2e}"
    print(mystring)
    myfile.write( mystring+'\n' )
    mystring = f"{phys_dict['dpdx']:.2e}\t{phys_dict['dpdy']:.2e}\t{phys_dict['dpdz']:.2e}"
    print(mystring)
    myfile.write( mystring+'\n' )
    mystring = f"{phys_dict['grx']:.2e}\t{phys_dict['gry']:.2e}\t{phys_dict['grz']:.2e}"
    print(mystring)
    myfile.write( mystring )

    # Methode brute avec uniquement des strings
    """
    lines = list('')
    lines.append("    1.00E+00   1.50E-05  0.0E+00 # ro1, xmu1, xmut1  (FLUIDE = AIR a 20°C)")
    lines.append("    -1.0025E+01   0.00E+00  0.0E+00   # dpdx, dpdy, dpdz")
    lines.append("    -2.5075E-02  -9.81E+00  0.0E+00	# grx, gry, grz")
    for i in range( len(lines) ):
        myfile.write( lines[i]+"\n" )
    """

    myfile.close()
    print(f"File " + colored(f"{myfilename}", "yellow") + " processed")

#------------------------------------------------------------------------------
#                       Serious stuff begin here
#------------------------------------------------------------------------------

dirname = "fichiers_config/"
case_name = "pois"
init_dict, phys_dict = dictionaries()
write_init_file()
write_phys_file()
