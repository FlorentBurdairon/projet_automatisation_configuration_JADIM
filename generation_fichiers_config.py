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
def para():
    para_dict = {
            "i3d": 0,
            "ixaxsy": 0,
            "icur": 0,
            "ijob": 0,
            "maxit": 1,
            "npi": 1,
            "ilist": 0,
            "ibin": 1,
            "ivort": 0,
            "itec": 0,
            "idat": 0,
            "reli": 'seq',
            "ebin": 'seq',
            "isolverp": 3,
            "epsip": 1.0e-8,
            "dtmin": 0.1e-7,
            "dtmax": 1.,
            "div": 1.5,
            "imp": 1,
            "iparacalc": 0,
            "ista": 6,
            "alf": 0.,
            "iles": 0,
            "imod": 5,
            "cconst": 0.,
            "constt": 0.,
            "it": 0,
            "irt": 0,
            "irovar": 1,
            "istat": 0,
            "ijobstat": 0,
            "npsdeb": 0,
            "itraj": 0,
            "irtraj": 0,
            "ipertur": 0,
            "nptper": 0,
            "nptperdeb": 0,
            "typeper": 0,
            "icoupl": 0,
            "igaz": 0,
            "idatr": 0,
            "ibm": 0,
            "ichim": 0,
            "irchim": 0,
            "irheo": 0,
            "idem": 0,
            "ifcm": 0,
            }
    return para_dict

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
def rovar():
    rovar_dict = {
            "nphase": 2,
            "iro": 2,
            "ro1": 1.,
            "xmu1": 1.5e-5,
            "xmut1": 0.,
            "ro2": 1.0e+3,
            "xmu2": 1.0e-3,
            "xmut2": 0.,
            "ro3": 0.,
            "xmu3": 0.,
            "xmut3": 0.,
            "idm": 0,
            "dm": 0.,
            "ifick": 0,
            "idttensu": 1,
            "tensu12": 72.8e-3,
            "tensu13": 0.,
            "tensu23": 0.,
            "icoflis2": 6,
            "icoflis3": 6,
            "iwet": 0,
            "ihyst": 0,
            "iwdyn": 0,
            "iglis": 0,
            "imuhar": 1,
            "icoflis1": 0,
            "i_verif_masse": 1,
            "tcritere": 1e-3,
            "masse_init": 0.,
            "i_modif_vitesse": 0,
            "isurf": 0,
            "C_surf0": 1,
            "C_surfmax": 1,
            "i_mcorr": 0,
            "i_Diff": 0,
            "D_Coeff": 0,
            "i_source": 0,
            "K_a": 0,
            "K_d": 0,
            "i_sigvar": 0,
            "i_sigma_init": 1,
            }
    return rovar_dict

#==================================================================================================
# ASSEMBLE STRINGS
#==================================================================================================
def init_strings():
    init_dict = init()

    mystrings = list()

    mystrings.append( assemble_string( {k:init_dict[k] for k in ('cu0', 'cux', 'cuy', 'cv0', 'cvx', 'cvy', 'omega') if k in init_dict} ) )
    mystrings.append( assemble_string( {k:init_dict[k] for k in ('tini', '') if k in init_dict} ) )
    mystrings.append( assemble_string( {k:init_dict[k] for k in ('ishear', '') if k in init_dict} ) )
    mystrings.append( assemble_string( {k:init_dict[k] for k in ('iswirl', '') if k in init_dict} ) )
    mystrings.append( assemble_string( {k:init_dict[k] for k in ('icomb', 'nnwave') if k in init_dict} ) )
    mystrings.append( assemble_string( {k:init_dict[k] for k in ('nwave', 'nwaveout') if k in init_dict} ) )
    mystrings.append( assemble_string( {k:init_dict[k] for k in ('nblock', '') if k in init_dict} ) )
    mystrings.append( assemble_string( {k:init_dict[k] for k in ('xdeb', 'xfin', 'ydeb', 'yfin', 'zdeb', 'zfin', 'tauini2', 'tauini3') if k in init_dict} ) )

    return mystrings

#==================================================================================================
def para_strings():
    para_dict = para()

    mystrings = list()

    mystrings.append( assemble_string( {k:para_dict[k] for k in ('i3d', 'ixaxsy', 'icur') if k in para_dict} ) )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('ijob', '') if k in para_dict} ) )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('maxit', '') if k in para_dict} ) )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('npi', 'ilist', 'ibin', 'ivort', 'itec', 'idat') if k in para_dict} ) )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('reli', 'ebin') if k in para_dict} ) )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('isolverp', 'epsip') if k in para_dict} ) )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('dtmin', 'dtmax', 'div') if k in para_dict} ) )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('imp', '') if k in para_dict} ) )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('iparacalc', '') if k in para_dict} ) )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('ista', 'alf') if k in para_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('iles', 'imod', 'cconst', 'constt') if k in para_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('it', 'irt') if k in para_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('irovar', '') if k in para_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('istat', 'ijobstat', 'npsdeb') if k in para_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('itraj', 'irtraj') if k in para_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('ipertur', 'nptper', 'nptperdeb', 'typeper') if k in para_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('icoupl', 'igaz') if k in para_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('idatr', '') if k in para_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('ibm', '') if k in para_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('ichim', 'irchim') if k in para_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('irheo', 'idem') if k in para_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('idem', '') if k in para_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:para_dict[k] for k in ('ifcm', '') if k in para_dict} ) )

    return mystrings

#==================================================================================================
def phys_strings():
    phys_dict = phys()

    mystrings = list()

    mystrings.append( assemble_string( {k:phys_dict[k] for k in ('ro1', 'xmu1', 'xmut1') if k in phys_dict} ) )
    mystrings.append( assemble_string( {k:phys_dict[k] for k in ('dpdx', 'dpdy', 'dpdz') if k in phys_dict} ) )
    mystrings.append( assemble_string( {k:phys_dict[k] for k in ('grx', 'gry', 'grz') if k in phys_dict} ) )

    return mystrings

#==================================================================================================
def rovar_strings():
    rovar_dict = rovar()

    mystrings = list()

    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('nphase', '') if k in rovar_dict} ) )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('iro', '') if k in rovar_dict} ) )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('ro1', 'xmu1', 'xmut1') if k in rovar_dict} ) )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('ro2', 'xmu2', 'xmut2') if k in rovar_dict} ) )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('ro3', 'xmu3', 'xmut3') if k in rovar_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('idm', 'dm', 'ifick') if k in rovar_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('idttensu', '') if k in rovar_dict} ) )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('tensu12', 'tensu13', 'tensu23') if k in rovar_dict} ) )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('icoflis2', 'icoflis3') if k in rovar_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('iwet', 'ihyst', 'iwdyn', 'iglis') if k in rovar_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('imuhar', 'icoflis1') if k in rovar_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('i_verif_masse', 'tcritere', 'masse_init') if k in rovar_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('i_modif_vitesse', '') if k in rovar_dict} ) )
    mystrings.append( separation )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('isurf', 'C_surf0', 'C_surfmax', 'i_mcorr') if k in rovar_dict} ) )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('i_Diff', 'D_Coeff') if k in rovar_dict} ) )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('i_source', 'K_a', 'K_d') if k in rovar_dict} ) )
    mystrings.append( assemble_string( {k:rovar_dict[k] for k in ('i_sigvar', 'i_sigma_init') if k in rovar_dict} ) )

    return mystrings

#==================================================================================================
def assemble_string( mydico ):
    mystring = ' ' # start line with a white space
    sp = ' '
    N = 60
    # write parameters values
    for item in mydico:
        value = mydico[item]
        if isinstance( value, float ) and value != 0:
            mystring += f"{value:e}" + sp*3
        else:
            mystring += f"{value}" + sp*3
    # write parameters names as comments
    mystring = '{:70}'.format(mystring) # add as many white spaces so the length of the string is 70
    mystring += '#' + sp*2
    for item in mydico:
        mystring += f"{item}" + ',' + sp
    mystring += '\n'
    return mystring

#==================================================================================================
# WRITE STRINGS TO CONFIG FILES
#==================================================================================================
def write_to_file( config ):
    if not( config in list_of_config_files ):
        print("[Error] " + colored( config, "red") + " is not an appropriate config file name")
        return
    else:
        filename = dirname + case_name + '.' + config
        myfile = open( filename, 'w')

        list_of_strings = func_options[config]()
        for item in list_of_strings:
            myfile.write( item )

        myfile.close()
        print(f"File " + colored(f"{config}", "yellow") + " processed")

#==================================================================================================
# SERIOUS STUFF BEGIN HERE
#==================================================================================================

dirname = "fichiers_config/"
case_name = "surf"

# artificial separation that is mandatory at some places in some config files (why? dunno)
separation = "---------------------------------------------------------------------\n"
list_of_config_files = ['init', 'para', 'phys', 'rovar']
func_options = {
        'init': init_strings,
        'para': para_strings,
        'phys': phys_strings,
        'rovar': rovar_strings,
        }

write_to_file( "init" )
write_to_file( "para" )
write_to_file( "phys" )
write_to_file( "rovar" )
