'''
Author:   Richard D. Pohl
Date:     April, 2024
Summary:  Build and Report on a Prime Composite Particle
'''

import refitems as ri
import prtfunction as prt

def prime_size_and_mass(item_refs_list, item_pass_list, fp):
    """Version 1.0.0: Initial Release"""

    item_eff_number   = ri.find_record(item_pass_list, 'Level III Effective')
    item_eff_size     = item_pass_list[item_eff_number].size
    item_eff_count    = item_pass_list[item_eff_number].mass

    item_ineff_number = ri.find_record(item_pass_list, 'Level III Ineffective')
    item_ineff_size   = item_pass_list[item_ineff_number].size
    item_ineff_count  = item_pass_list[item_ineff_number].mass

    item_comp_number  = ri.find_record(item_pass_list, 'Level III Comp')
    item_comp_size    = item_pass_list[item_comp_number].size
    item_comp_count   = item_pass_list[item_comp_number].mass

    hydrogen:    int = 6
    sun:         int = 2
    solar_sys:   int = 1
    galaxy:      int = 0

    level_three: int = sun
    prime:       int = solar_sys
    
    #now project sizeof Level II Composite Particle
    #get drill-down factor as size of hyrdrogen to galaxy size
    cp_prime_size_factor = item_refs_list[prime].size / item_refs_list[galaxy].size
    
    #use the factor and drill down from hydrogen to determine {f} size/
    cp_prime_size = item_refs_list[hydrogen].size * cp_prime_size_factor
    
    lvl_3_cp_size_factor   = item_refs_list[level_three].size / item_refs_list[galaxy].size
    
    lvl_3_cp_size   = item_refs_list[hydrogen].size * lvl_3_cp_size_factor
    lvl_3_comp_size = item_refs_list[hydrogen].size * lvl_3_cp_size_factor

    count_of_prm_in_lvl_3_by_size  = cp_prime_size /  lvl_3_cp_size
    
    prtstr = "Advanced Level III Composite Particle Summary \n"
    prt.prt_function(fp, prtstr)
    prt.prt_function(fp, "Projections of Size \n")
    prt.prt_function(fp, f"In Regular Level III Units{' ':>24}size {cp_prime_size:5.3e}  \n")  
    prt.prt_function(fp, f"In Regular Level III Units{' ':>15}count by size {count_of_prm_in_lvl_3_by_size:5.3e}  \n") 
    prt.prt_function(fp, "  \n")

    #now process calculated values
    prime_eff_size   = item_eff_count * item_eff_size
    prime_ineff_size = item_ineff_count * item_ineff_size
    comp_eff_size    = item_comp_count * item_comp_size 

    count_of_eff_prime_in_lvl_3_by_size   = cp_prime_size / item_eff_size
    count_of_ineff_prime_in_lvl_3_by_size = cp_prime_size / item_ineff_size
    count_of_comp_in_lvl_3_by_size        = cp_prime_size / item_comp_size

    prt.prt_function(fp, "Calculated Sizes\n") 
    prt.prt_function(fp, "Effective\n")
    prt.prt_function(fp, f"Advanced Level III CP{' ':>29}size {prime_eff_size:5.3e}  \n") 
    prt.prt_function(fp, f"Advanced Level III Units{' ':>17}count by size {count_of_eff_prime_in_lvl_3_by_size:5.3e}  \n") 
    
    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "Ineffective\n")
    prt.prt_function(fp, f"Advanced Level III CP{' ':>29}size {prime_ineff_size:5.3e}  \n") 
    prt.prt_function(fp, f"Advanced Level III Units{' ':>17}count by size {count_of_ineff_prime_in_lvl_3_by_size:5.3e}  \n")  
    
    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "Complementary\n")
    prt.prt_function(fp, f"Complementary CP{' ':>34}size {item_comp_size:5.3e}  \n")  
    prt.prt_function(fp, f"Complementary in Level III Unitss{' ':>8}count by size {count_of_comp_in_lvl_3_by_size:5.3e}  \n") 
        
    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")

    item_pass_list.append(ri.PassItems('Advanced Level III Effective', prime_eff_size, 0 )) 
    item_pass_list.append(ri.PassItems('Advanced Level III Ineffective', prime_ineff_size, 0)) 
    item_pass_list.append(ri.PassItems('Advanced Level III Comp', comp_eff_size, 0)) 

    return(item_refs_list, item_pass_list)
