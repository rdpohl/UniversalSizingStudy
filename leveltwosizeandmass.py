'''
Author:   Richard D. Pohl
Date:     April, 2024
Summary:  Build and Report on a Level Two Composite Particle
'''

import random
import refitems as ri
import prtfunction as prt

def level_2_size_and_mass(item_refs_list, item_pass_list, fp):
    """Version 1.0.0: Initial Release"""

    item_number = ri.find_record(item_pass_list, 'Level I')
    item_size   = item_pass_list[item_number].size
    item_mass   = item_pass_list[item_number].mass

    hydrogen:  int = 6
    planet:    int = 3
    galaxy:    int = 0

    level_two: int = planet

    prt.prt_function(fp, "  \n")

    #now project size of Level II Composite Particle
    cvp_2_size_factor = item_refs_list[level_two].size / item_refs_list[galaxy].size
    
    #use the factor and drill down from hydrogen to determine {f} size
    cp_lvl_2_size = item_refs_list[hydrogen].size * cvp_2_size_factor
    
    count_of_lvl_1_in_lvl_2_by_size = cp_lvl_2_size /  item_size
    
    prtstr = "Level II Composite Particle Summary of Size\n" 
    prt.prt_function(fp, prtstr)
    prt.prt_function(fp, "Projections of Size\n") 
    prt.prt_function(fp, f"Level II CP in Level I Units{' ':>22}size {cp_lvl_2_size:5.3e}  \n")   
    prt.prt_function(fp, f"Level II CP In Level I Units{' ':>13}count by size {count_of_lvl_1_in_lvl_2_by_size:5.3e}  \n")  
    prt.prt_function(fp, "  \n")

    #calculated values
    #-----------------------------------------------------------------------------------------
    size1, mass1 = return_particle_size_mass("Series", item_size, item_mass)
    size2, mass2 = return_particle_size_mass("Series", item_size, item_mass)
   
    #average the two sizes 
    tot_size_12_avg = (size1 + size2) / 2 
   
    prt.prt_function(fp, "Calculated Size\n") 
    prt.prt_function(fp, "Series Join - Sample Size of Two Level 1 Particles X and Y\n")
    prt.prt_function(fp, f"     Level I Particle X {' ':>26}size {size1:5.3e}  \n")   
    prt.prt_function(fp, f"     Level I Particle Y {' ':>26}size {size2:5.3e}  \n")   
    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, f"     Level I Particle X, Y Average** {' ':>13}size {tot_size_12_avg:5.3e}  \n")  
    prt.prt_function(fp, "  \n")

    size3, mass3 = return_particle_size_mass("Quantitative", item_size, item_mass)
    size4, mass4 = return_particle_size_mass("Quantitative", item_size, item_mass)
    
    # average the two sizes 
    tot_size_34_avg = (size3 + size4) / 2 
    tot_mass_34_avg = (mass3 + mass4) / 2

    prt.prt_function(fp, "Quantitative Join - Sample Size of Two Level 1 Particles X and Y\n")
    prt.prt_function(fp, f"     Level I Particle X {' ':>26}size {size3:5.3e}  \n")  
    prt.prt_function(fp, f"     Level I Particle Y {' ':>26}size {size4:5.3e}  \n")  
    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, f"     Level I Particle X, Y Average** {' ':>13}size {tot_size_34_avg:5.3e}  \n")  
    prt.prt_function(fp, "  \n")

    prt.prt_function(fp, "** Will carry these Individual values, for  series and quantitative particles, to  \n")
    prt.prt_function(fp, "   Level III where they will be applied as groups. \n")
    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")
    
    item_pass_list.append(ri.PassItems('Level II 12SAM', tot_size_12_avg, 0 )) 
    item_pass_list.append(ri.PassItems('Level II 34SAM', tot_size_34_avg, 0 )) 

    return item_refs_list, item_pass_list

def return_particle_size_mass(str_type, init_size, init_mass):
    """
    Version 1.0.0: Initial Release
    Each if-else section has the ability to customize sizes by changing the 
    two numbers in the call to random.uniform
    init_size * 0.3 means that it will return that percent size/mass of the 
    projected Level II size/mass
    """

    if str_type == "Series":
        # consider size as a count of particles in the series matrix, not the
        # size of the ouside dimensions 
        size = random.uniform(init_size * 0.1, init_size * 0.3)
        mass = 0 
    else:
        #Quantitative
        size = random.uniform(init_size * 0.8, init_size * 1.0)
        mass = 0 

    return(size, mass)
