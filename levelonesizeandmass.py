'''
Author:   Richard D. Pohl
Date:     April, 2024
Summary:  Build and Report on a Level One Composite Particle 
'''

import math
import refitems as ri
import prtfunction as prt

def level_1_size_and_mass(item_refs_list, item_pass_list, fp):
    """Version 1.0.0 Initial Release"""

    prt.prt_function(fp, "  \n")

    hydrogen:  int = 6
    asteroid:  int = 4
    galaxy:    int = 0

    level_one:  int = asteroid

    #get drill-down factor as size of hyrdrogen to galaxy size
    f_size_factor = item_refs_list[hydrogen].size / item_refs_list[galaxy].size
    
    #use the factor and drill down from hydrogen to determine {f} size
    f_size = item_refs_list[hydrogen].size * f_size_factor
    
    #get drill-down factor for Composite Particle Level I size
    lvl_1_cp_size_factor = item_refs_list[level_one].size / item_refs_list[galaxy].size
    
    #use factor and drill-down from hydrogen to dertermine CP-LvlI size
    lvl_1_cp_size = item_refs_list[hydrogen].size * lvl_1_cp_size_factor  #projected
    
    #Calculate Projected sizing for a Level I Composite Particle
    count_of_f_in_lvl_1_by_size = lvl_1_cp_size / f_size  #from projected
    
    #calculate rather than project the CP Lvl I size 
    #the particles of f form into a single, loosely connected composite particle

    prtstr = "Level I Composite Particle Summary of Sizes\n"
    prt.prt_function(fp, prtstr)
    prt.prt_function(fp, "Projections of Sizes\n")
    prt.prt_function(fp, f"Level I CP by size: {{f}}{' ':>33}{lvl_1_cp_size:5.3e} \n")  
    prt.prt_function(fp, f"Level I CP by count: {{f}}{' ':>31}{count_of_f_in_lvl_1_by_size:5.3e}* A\n")  
    prt.prt_function(fp, "  \n")
    
    #calculating size of sub-f particles
    #build Level I CP by size, add a bit loose pack via fluff factor

    fluff_factor       = 1.5
    tot_level_1_size   = count_of_f_in_lvl_1_by_size * (f_size * fluff_factor)
    
    prt.prt_function(fp, "Calculated Size\n") 
    prt.prt_function(fp, f"Expasion Factor (due to sub-f particles):{' ':>14}{fluff_factor:5.3e}  B \n") 
    prt.prt_function(fp, f"Size of {{f}} particle:{' ':>34}{f_size:5.3e}  C \n") 
    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, f"Level I CP:{' ':>36}(A*B*C) {tot_level_1_size:5.3e}  E \n") 
    prt.prt_function(fp, "  \n")

    # calc force details
    # say a & b are members of {f}. b is 2 f-lengths away and collideds with a at its mid-point
    distance  = 2 * f_size           #distance a travels to collide with b
    contpnt   = f_size / 2           #a contacts b at its midpoint
    speed     = distance / contpnt

    rate_of_sub_f         = 0.10  #sub-f in 1 of every 10 collisions
    nbr_of_sub_f          = count_of_f_in_lvl_1_by_size * rate_of_sub_f
    
    #sub-f size x% of full size {f}
    percent_factor        = 0.15     # % of f-size from collision breakage
    exp_from_ke           = 5.0      # sub-f movement worth x sub-f particles
    per_sub_f_size        = f_size * percent_factor
    tot_lvl_1_sub_f_size  = (count_of_f_in_lvl_1_by_size * per_sub_f_size) * exp_from_ke

    prt.prt_function(fp, f"Per sub-size:{' ':>42}{f_size:5.3e}  F \n") 
    prt.prt_function(fp, f"Expansion Factor:{' ':>38}{f_size:5.3e}  G \n") 
    prt.prt_function(fp, f"Total Sub-f by size:{' ':>27}(A*F*G) {tot_lvl_1_sub_f_size:5.3e} \n")  
    
    #now total full and sub-f size
    tot_lvl_1_size        = tot_level_1_size + tot_lvl_1_sub_f_size
    
    prt.prt_function(fp, f"{' ':>55}{'---------'} \n")  
    prt.prt_function(fp, f"Level I Composite Particle{' ':>24}size {tot_lvl_1_size:5.3e} \n") 

    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "Itemized Details\n")
    prt.prt_function(fp, f"Count {{f}} in Level:{' ':>36}{count_of_f_in_lvl_1_by_size:5.3e}* \n") 
    prt.prt_function(fp, f"Sub-f Percent Size of {{f}}:{' ':>33}{percent_factor:.2%}\n")
    prt.prt_function(fp, f"Sub-f Rate of Collisions:{' ':>34}{rate_of_sub_f:.2%}\n")
    prt.prt_function(fp, f"Count Sub-f in Level:{' ':>34}{nbr_of_sub_f:5.3e}\n")
    

    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "*Values are the same.  \n")
    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")

    item_pass_list.append(ri.PassItems('Level I', tot_lvl_1_size, 0 ))  
    item_pass_list.append(ri.PassItems('Level I Counts', count_of_f_in_lvl_1_by_size, 0 ))

    return item_refs_list, item_pass_list
