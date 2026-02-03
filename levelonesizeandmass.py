'''
Author:   Richard D. Pohl
Date:     April, 2024
Summary:  Build and Report on a Level One Composite Particle 
'''

import math
import readjson as rj
import refitems as ri
import prtfunction as prt

def level_1_size_and_mass(item_refs_list, item_pass_list, json_ptr, fp):
    """Version 1.0.0 Initial Release"""

    #prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "  \n")

    hydrogen:  int = 6
    asteroid:  int = 4
    galaxy:    int = 0

    level_one:  int = asteroid

    with open(json_ptr, "r") as f:
       reader = rj.JSONReader(json_ptr)
       if reader.read_json_file():
            # Access data using standard dictionary syntax or the helper method
            fluff_factor   = reader.get_value(['levelone','fluff'])
            percent_factor = reader.get_value(['levelone','percent_factor'])
            exp_from_ke    = reader.get_value(['levelone','exp_from_ke']) 

    #get drill-down factor as size/mass of hyrdrogen to galaxy size/mass
    f_size_factor = item_refs_list[hydrogen].size / item_refs_list[galaxy].size
    f_mass_factor = item_refs_list[hydrogen].mass / item_refs_list[galaxy].mass

    #use the factor and drill down from hydrogen to determine {f} size/mass
    f_size = item_refs_list[hydrogen].size * f_size_factor
    f_mass = item_refs_list[hydrogen].mass * f_mass_factor

    #get drill-down facor for Composite Particle Level I size/mass
    lvl_1_cp_size_factor = item_refs_list[level_one].size / item_refs_list[galaxy].size
    lvl_1_cp_mass_factor = item_refs_list[level_one].mass / item_refs_list[galaxy].mass

    #use factor and drill-down from hydrogen to dertermine CP-LvlI size/mass
    lvl_1_cp_size = item_refs_list[hydrogen].size * lvl_1_cp_size_factor  #projected
    lvl_1_cp_mass = item_refs_list[hydrogen].mass * lvl_1_cp_mass_factor  #projected

    #Calculate Projected sizing and mass for a Level I Composite Particle
    #get counts
    count_of_f_in_lvl_1_by_size = lvl_1_cp_size / f_size  #from projected
    count_of_f_in_lvl_1_by_mass = lvl_1_cp_mass / f_mass  #from projected

    #calculate rather than project the CP Lvl I size and mass
    #the particles of f form into a single, loosely connected composite particle

    prtstr = "Level I Composite Particle Summary of Sizes\n"
    prt.prt_function(fp, prtstr)
    prt.prt_function(fp, "Projections of Sizes\n")
    prt.prt_function(fp, f"Level I CP by size: {{f}}{' ':>33}{lvl_1_cp_size:5.3e} \n")  #{' ':>19}mass {lvl_1_cp_mass:5.3e}\n")
    prt.prt_function(fp, f"Level I CP by count: {{f}}{' ':>31}{count_of_f_in_lvl_1_by_size:5.3e}* A\n")  #{' ':>17}count {count_of_f_in_lvl_1_by_mass:5.3e}*\n")
    prt.prt_function(fp, "  \n")
    
    #calculating size/mass of sub-f particles
    #build Level I CP by size, add a bit loose pack via fluff factor

    #fluff_factor       = 1.5
    tot_level_1_size   = count_of_f_in_lvl_1_by_size * (f_size * fluff_factor)
    tot_level_1_mass   = count_of_f_in_lvl_1_by_mass * f_mass

    prt.prt_function(fp, "Calculated Size\n") # and Mass\n")
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

    #now get angular velocity
    part_f_m1 = f_mass    #mass in kg
    part_f_v1 = speed     #particle 1 is moving meters/second

    part_f_m2 = f_mass    #mass in kg
    part_f_v2 = 0.0       #particle 2 velocity is zero

    # Kinetic Energy = 1/2 * m * v^2
    ke_final  = .5 * (part_f_m1 + part_f_m2) * pow((part_f_v1 + part_f_v2), 2)

    #calc sub-f mass from kinetic energy
    #sub-f mass = 2 * KE / velocity^2
    sub_f_mass            = 2 * (ke_final / math.pow(part_f_v1, 2))
    rate_of_sub_f         = 0.10  #sub-f in 1 of every 10 collisions

    nbr_of_sub_f          = count_of_f_in_lvl_1_by_size * rate_of_sub_f
    tot_sub_f_mass        = nbr_of_sub_f * sub_f_mass

    #sub-f size x% of full size {f}
    #percent_factor        = 0.15     # % of f-size from collision breakage
    #exp_from_ke           = 5.0      # sub-f movement worth x sub-f particles
    per_sub_f_size        = f_size * percent_factor
    tot_lvl_1_sub_f_size  = (count_of_f_in_lvl_1_by_size * per_sub_f_size) * exp_from_ke

    prt.prt_function(fp, f"Per sub-size:{' ':>42}{f_size:5.3e}  F \n") 
    prt.prt_function(fp, f"Expansion Factor:{' ':>38}{f_size:5.3e}  G \n") 
    prt.prt_function(fp, f"Total Sub-f by size:{' ':>27}(A*F*G) {tot_lvl_1_sub_f_size:5.3e} \n")  #{' ':>19}mass {tot_sub_f_mass:5.3e}\n")
    
    #now total full and sub-f size/mass
    tot_lvl_1_size        = tot_level_1_size + tot_lvl_1_sub_f_size
    tot_lvl_1_sub_f_mass  = tot_level_1_mass + tot_sub_f_mass

    prt.prt_function(fp, f"{' ':>55}{'---------'} \n")  #{' ':>24}{'---------'}\n")
    prt.prt_function(fp, f"Level I Composite Particle{' ':>24}size {tot_lvl_1_size:5.3e} \n")  #{' ':>19}mass {tot_lvl_1_sub_f_mass:5.3e}\n")

    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "Itemized Details\n")
    prt.prt_function(fp, f"Count {{f}} in Level:{' ':>36}{count_of_f_in_lvl_1_by_size:5.3e}* \n")  #{' ':>23}{count_of_f_in_lvl_1_by_mass:5.3e}*\n")
    prt.prt_function(fp, f"Sub-f Percent Size of {{f}}:{' ':>33}{percent_factor:.2%}\n")
    prt.prt_function(fp, f"Sub-f Rate of Collisions:{' ':>34}{rate_of_sub_f:.2%}\n")
    prt.prt_function(fp, f"Count Sub-f in Level:{' ':>34}{nbr_of_sub_f:5.3e}\n")
    #prt.prt_function(fp, f"Sub-f Mass from Kinetic Energy:{' ':>57}{sub_f_mass:5.3e}\n")

    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "*Values are the same.  \n")
    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")

    item_pass_list.append(ri.PassItems('Level I', tot_lvl_1_size, 0 ))   #tot_lvl_1_sub_f_mass))
    item_pass_list.append(ri.PassItems('Level I Counts', count_of_f_in_lvl_1_by_size, 0 )) #count_of_f_in_lvl_1_by_mass))

    return item_refs_list, item_pass_list
