'''
Author:   Richard D. Pohl
Date:     Aprile, 2024
Summary:  Calculate and report hypothesized sizes of prejected
          Universal Matter objects
'''

import prtfunction as prt

def drill_down_sizing(item_refs_list, fp):
    """Version 1.0.0: Initial Release"""

    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "  \n")

    hydrogen:  int = 6
    asteroid:  int = 4
    planet:    int = 3
    sun:       int = 2
    solar_sys: int = 1
    galaxy:    int = 0

    level_one:   int = asteroid
    level_two:   int = planet
    level_three: int = sun
    prime:       int = solar_sys

    #Relative factored size of {f} as hydrogen compared to the galaxy
    f_size_factor = item_refs_list[hydrogen].size / item_refs_list[galaxy].size
    f_size = item_refs_list[hydrogen].size * f_size_factor
    
    prtstr = "Summary of Calculated Projections by Size of Universal Matter Objects\n"
    prt.prt_function(fp, prtstr)
    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")
    prt.prt_function(fp, f"The size of a particle of {{f}} is{' ':>23}{f_size:2.3e} \n") 

    #Relative size of the three levels of Composite Particles
    #The smallest, Level I
    lvl_1_cp_size_factor = item_refs_list[level_one].size / item_refs_list[galaxy].size
    lvl_1_cp_size = item_refs_list[hydrogen].size * lvl_1_cp_size_factor
    
    # Mid point, Level II
    lvl_2_cp_size_factor = item_refs_list[level_two].size / item_refs_list[galaxy].size
    lvl_2_cp_size = item_refs_list[hydrogen].size * lvl_2_cp_size_factor
    
    # Biggest point, Level III
    lvl_3_cp_size_factor = item_refs_list[level_three].size / item_refs_list[galaxy].size#
    lvl_3_cp_size = item_refs_list[hydrogen].size * lvl_3_cp_size_factor
    
    prt.prt_function(fp, f"The size of a Level I Composite Particle is {' ':>11}{lvl_1_cp_size:5.3e} \n") 
    prt.prt_function(fp, f"The size of a Level II Composite Particle is {' ':>10}{lvl_2_cp_size:5.3e} \n")
    prt.prt_function(fp, f"The size of a Level III Composite Particle is {' ':>9}{lvl_3_cp_size:5.3e} \n")

    #Relative factored size of Advanced Level III Particle as our sun compared to the galaxy
    prime_size_factor = item_refs_list[prime].size / item_refs_list[galaxy].size
    prime_size = item_refs_list[hydrogen].size * prime_size_factor 
    
    prt.prt_function(fp, f"The size of an Advanced Level III Particle is {' ':>9}{prime_size:5.3e} \n") 
    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")

    return item_refs_list
