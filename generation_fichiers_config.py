# python librairies
import numpy as np
import matplotlib.pyplot as plt
from termcolor import colored
import os

#====================================================================================
# DEFINE CONFIG PARAMETERS AND PHYSICAL PROPERTIES
#==================================================================================================
def init():
    init_dict = {
            "cu0": 0.,
            "cux": 0.,
            "cuy": 0.,
            "cv0": 0.,
            "cvx": 0.,
            "cvy": 0.,
            "omega": 0.,
            "tini": 0.,
            "ishear": 0,
            "iswirl": 0,
            "icomb": 0,
            "nnwave": 1,
            "nwave": 10,
            "nwaveout": 0,
            "nblock": 1,
            "xdeb": 0.0,
            "xfin": 200e-3,
            "ydeb": 0.0,
            "yfin": 25e-3,
            "zdeb": 0.0,
            "zfin": 1.0,
            "tauini2": 1.0,
            "tauini3": 0.0,
        }
    return init_dict

#==================================================================================================
def phys():
    phys_dict = {
            "ro1": 1.,
            "xmu1": 1.5e-5,
            "xmut1": 0.,
            "dpdx": -1.0025E+01,
            "dpdy": 0.,
            "dpdz": 0.,
            "grx": -2.5075E-02,
            "gry": -9.81,
            "grz": 0.,
            }
    return phys_dict

#==================================================================================================
# ASSEMBLE STRINGS
#==================================================================================================
def write_init_file():
    init_dict = init()

    myfilename = ".init"
    myfile = open( dirname + case_name + myfilename, "w")

    myfile.write( assemble_string( {k:init_dict[k] for k in ('cu0', 'cux', 'cuy', 'cv0', 'cvx', 'cvy', 'omega') if k in init_dict} ) )
    myfile.write( assemble_string( {k:init_dict[k] for k in ('tini', '') if k in init_dict} ) )
    myfile.write( assemble_string( {k:init_dict[k] for k in ('ishear', '') if k in init_dict} ) )
    myfile.write( assemble_string( {k:init_dict[k] for k in ('iswirl', '') if k in init_dict} ) )
    myfile.write( assemble_string( {k:init_dict[k] for k in ('icomb', 'nnwave') if k in init_dict} ) )
    myfile.write( assemble_string( {k:init_dict[k] for k in ('nwave', 'nwaveout') if k in init_dict} ) )
    myfile.write( assemble_string( {k:init_dict[k] for k in ('nblock', '') if k in init_dict} ) )
    myfile.write( assemble_string( {k:init_dict[k] for k in ('xdeb', 'xfin', 'ydeb', 'yfin', 'zdeb', 'zfin', 'tauini2', 'tauini3') if k in init_dict} ) )

    myfile.close()
    print(f"File " + colored(f"{myfilename}", "yellow") + " processed")

#==================================================================================================
def write_phys_file():
    phys_dict = phys()

    myfilename = ".phys"
    myfile = open( dirname + case_name + myfilename, "w")

    myfile.write( assemble_string( {k:phys_dict[k] for k in ('ro1', 'xmu1', 'xmut1') if k in phys_dict} ) )
    myfile.write( assemble_string( {k:phys_dict[k] for k in ('dpdx', 'dpdy', 'dpdz') if k in phys_dict} ) )
    myfile.write( assemble_string( {k:phys_dict[k] for k in ('grx', 'gry', 'grz') if k in phys_dict} ) )

    myfile.close()
    print(f"File " + colored(f"{myfilename}", "yellow") + " processed")

#==================================================================================================
def assemble_string( mydico ):
    mystring = ' '
    sp = ' '
    N = 60
    for item in mydico:
        value = mydico[item]
        if isinstance( value, float ) and value != 0:
            mystring += f"{value:e}" + sp*3
        else:
            mystring += f"{value}" + sp*3
    mystring = '{:100}'.format(mystring)
#    if len(mystring) < N:
#        mystring += sp*(N-len(mystring))
    mystring += '#' + sp*2
    for item in mydico:
        mystring += f"{item}" + ',' + sp
    mystring += '\n'
#    print( mystring )
    return mystring

#==================================================================================================
# SERIOUS STUFF BEGIN HERE
#==================================================================================================

dirname = "fichiers_config/"
case_name = "pois"

write_init_file()
write_phys_file()

