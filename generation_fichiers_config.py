############################################################################################################
# Script python that generates some configuration files needed to compute a diphasic simulation with JADIM #
############################################################################################################

# python librairies
import numpy as np
from termcolor import colored
import os

#===================================================================================================
# DEFINE CONFIG PARAMETERS AND PHYSICAL PROPERTIES
#===================================================================================================
def init():
    init_dict = {
            # vitesse initiale selon x : u = cu0 + cux * x + cuy + y
            # vitesse initiale selon y : v = cv0 + cvx * x + cvy + y
            # vitesse initiale selon z : w = omega
            # div(u) = cux + cvy = 0
            "cu0": 0.,
            "cux": 0.,
            "cuy": 0.,
            "cv0": 0.,
            "cvx": 0.,
            "cvy": 0.,
            "omega": 0.,
            "tini": 0., # temperature intiale
            "ishear": 0, # type d adimensionalisation des coefficient de trainee et portance
            "iswirl": 0, # creation d'un tourbillon si =1
            "icomb": 0, # type d initialisation pour densite variable (=0 pour ro constant)
            "nnwave": 1, #
            "nwave": 10, # initialise le taux de presence (1 selon le numero de cellule (i,j,k), 10 selon les coordonnees (x,y,z))
            "nwaveout": 0, #
            "nblock": 1, # nombre de carres ou cubes a initialiser (mettre 1 pour initialiser le 2nd fluide si diphasique)
            # si nwave = 10 et nblock = 1 : initialise le taux de presence de la 2nde phase dans un bloc delimite par les coordonnees xdeb<x<xfin, ydeb<y<yfin, zdeb<z<zfin
            "xdeb": 0.0,
            "xfin": 200e-3,
            "ydeb": 0.0,
            "yfin": 25e-3,
            "zdeb": 0.0,
            "zfin": 1.0,
            "tauini2": 1.0, # valeur du taux de presence de la 2nde phase dans le bloc defini ci-dessus
            "tauini3": 0.0, # valeur du taux de presence de la 2nde phase dans le bloc defini ci-dessus
        }
    return init_dict

#===================================================================================================
def para():
    para_dict = {
            "i3d": 0, # 1 if 3D
            "ixaxsy": 0, # 1 if axisymmetric
            "icur": 0, # 1 if curvilinear
            "ijob": 0, # 1 if computation restart, 2 to restart without Navier-Stokes
            "maxit": 1, # maximum number of iterations
            "npi": 1, # screen print (mass loss && npt,dt,du,dv,dw,dtau)
            "ilist": 0, # velocity field in ruvp (ascii format)
            "ibin": 1, # jadim binary in rbin (u,v,w,p,tempe,tau2)
            "ivort": 0, # vorticity field in rbinv binary file
            "itec": 0, # tecplot binary
            "idat": 0, # user variable for output
            "reli": 'seq', # seq, spl, mpi
            "ebin": 'seq', # seq, spl, mpi
            "isolverp": 3, # pressure solver choice - Fourier 1, itpack 2, PetsC 3
            "epsip": 1.0e-8, # stop criterium for iterative solver (2 or 3)
            "dtmin": 0.1e-7, # minimal time step
            "dtmax": 1., # maximal time step (imposed if dtCFL>dtmax)
            "div": 1.5, # security for CFL time step computed in the code : dt=dtCFL/div
            "imp": 1, # diffusivity treatment : 0 if explicit, 1 if implicit
            "iparacalc": 0, #
            "ista": 6, # flow type
            "alf": 0., # caracteristic value for flow (cf. front,forcage and traine.f90)
            "iles": 0, # Large Eddy Simulation if 1
            "imod": 5, # used LES model (1,2,3,4)
            "cconst": 0., # turbulent viscosity constant (if imod = 1 or 4)
            "constt": 0., # turbulent diffusivity constant (if imod = 1 or 4)
            "it": 0, # thermics calculus if si 1
            "irt": 0, # restart thermics
            "irovar": 1, # variable density (mono or polyphasic) if 1 (add a *.rovar input file)
            "istat": 0, # compute statistics if 1
            "ijobstat": 0, #  1 if stat on particles restart
            "npsdeb": 0, # statistics start time step
            "itraj": 0, # lagrangian particles tracking if 1 (add a *.traj input file)
            "irtraj": 0, # 1 if lagrangian particles tracking restart
            "ipertur": 0, # flow disturbance if > 0 (cf. 1:perturb/2:forcage)
            "nptper": 0, # number of disturbed iterations
            "nptperdeb": 0, # initial disturbed time step
            "typeper": 0, #
            "icoupl": 0, # 2-domains coupling
            "igaz": 0, # 0 for the fluid domain, 1 for the gaz domain
            "idatr": 0, # 1 to compute drag force (add *.datr input file)
            "ibm": 0, # 1 to add an immersed obstacle (add *.ibm input file)
            "ichim": 0, # 1 to compute reaction (add *.chim input file)
            "irchim": 0, # 1 to restart a chemistry computation
            "irheo": 0, # 1 to compute a non newtonian rheology (add *.rheo input file)
            "idem": 0, #
            "ifcm": 0, #
            }
    return para_dict

#===================================================================================================
def phys():
    phys_dict = {
            "ro1": 1., # density for phase 1
            "xmu1": 1.5e-5, # dynamic viscosity for phase 1
            "xmut1": 0., # thermic diffusivity for phase 1
            "dpdx": -1.0025E+01, # x component of pressure gradient
            "dpdy": 0., # y component of pressure gradient
            "dpdz": 0., # z component of pressure gradient
            "grx": -2.5075E-02, # x component of gravity
            "gry": -9.81, # y component of gravity
            "grz": 0., # z component of gravity
            }
    return phys_dict

#===================================================================================================
def rovar():
    rovar_dict = {
            "nphase": 2, # number of phases
            "iro": 2, # 1 for 2nd order centered scheme, 2 for FCT, 3 for WENO5 (if nbphase = 2 -> iro =2)
            "ro1": 1., # density for phase 1
            "xmu1": 1.5e-5, # dynamic viscosity for phase 1
            "xmut1": 0., # thermic diffusivity for phase 1
            "ro2": 1.0e+3, # density for phase 2
            "xmu2": 1.0e-3, # dynamic viscosity for phase 2
            "xmut2": 0., # thermic diffusivity for phase 2
            "ro3": 0., # density for phase 3
            "xmu3": 0., # dynamic viscosity for phase 3
            "xmut3": 0., # thermic diffusivity for phase 3
            "idm": 0, # switch for molecular diffusivity
            "dm": 0., # molecular diffusivity value
            "ifick": 0, #
            "idttensu": 1, # switch for surface tension
            "tensu12": 72.8e-3, # surface tension between phase 1 and 2
            "tensu13": 0., # surface tension between phase 1 and 3
            "tensu23": 0., # surface tension between phase 2 and 3
            "icoflis2": 6, # smoothing coefficient for suface tension computation
            "icoflis3": 6, # smoothing coefficient for suface tension computation
            "iwet": 0, #
            "ihyst": 0, # switch for hysteresis
            "iwdyn": 0, # switch for dynamical contact angle
            "iglis": 0, #
            "imuhar": 1, # switch for harmonic computation of viscosity
            "icoflis1": 0, # smoothing coefficient (for what?)
            "i_verif_masse": 1, # switch for mass conservation checking
            "tcritere": 1e-3, # relative precision of the mass conservation
            "masse_init": 0., # "initial mass" of one of the fluids (printed at the 1st time step on the screen, only used for restart of run)
            "i_modif_vitesse": 0, # switch to keep a stiff front between 2 phases
            "isurf": 0, #
            "C_surf0": 1, #
            "C_surfmax": 1, #
            "i_mcorr": 0, #
            "i_Diff": 0, #
            "D_Coeff": 0, #
            "i_source": 0, #
            "K_a": 0, #
            "K_d": 0, #
            "i_sigvar": 0, #
            "i_sigma_init": 1, #
            }
    return rovar_dict

#===================================================================================================
# ASSEMBLE STRINGS
#===================================================================================================
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

#===================================================================================================
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

#===================================================================================================
def phys_strings():
    phys_dict = phys()

    mystrings = list()

    mystrings.append( assemble_string( {k:phys_dict[k] for k in ('ro1', 'xmu1', 'xmut1') if k in phys_dict} ) )
    mystrings.append( assemble_string( {k:phys_dict[k] for k in ('dpdx', 'dpdy', 'dpdz') if k in phys_dict} ) )
    mystrings.append( assemble_string( {k:phys_dict[k] for k in ('grx', 'gry', 'grz') if k in phys_dict} ) )

    return mystrings

#===================================================================================================
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

#===================================================================================================
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

#===================================================================================================
# WRITE STRINGS TO CONFIG FILES
#===================================================================================================
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

#===================================================================================================
def generate_output_directory( mydirname ):
    print(f"Output directory for config files : " + colored(f"{os.path.abspath(mydirname)}", "yellow"))
    try:
        os.mkdir( mydirname )
        print("(" + colored("[Warning]", "red") + " directory does not exist, creating it right now)")
    except FileExistsError:
        print("(Directory already exists, proceeding normally)")

#===================================================================================================
# SERIOUS STUFF BEGIN HERE
#===================================================================================================

dirname = "./fichiers_config/"
generate_output_directory( dirname )
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
