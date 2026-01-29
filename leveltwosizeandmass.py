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

    item_number_sm = ri.find_record(item_pass_list, 'Level I Counts')
    item_s_size   = item_pass_list[item_number_sm].size
    item_m_mass   = item_pass_list[item_number_sm].mass

    hydrogen:  int = 6
    planet:    int = 3
    galaxy:    int = 0

    level_two: int = planet

    #now project size/mass of Level II Composite Particle
    cvp_2_size_factor = item_refs_list[level_two].size / item_refs_list[galaxy].size
    cvp_2_mass_factor = item_refs_list[level_two].mass / item_refs_list[galaxy].mass

    #use the factor and drill down from hydrogen to determine {f} size/mass
    cp_lvl_2_size = item_refs_list[hydrogen].size * cvp_2_size_factor
    cp_lvl_2_mass = item_refs_list[hydrogen].mass * cvp_2_mass_factor

    count_of_lvl_1_in_lvl_2_by_size = cp_lvl_2_size /  item_size
    #count_of_lvl_1_in_lvl_2_by_mass = cp_lvl_2_mass /  item_mass

    prtstr = "Level II Composite Particle Summary of Size\n" # and Mass\n"
    prt.prt_function(fp, prtstr)
    prt.prt_function(fp, "Projections of Size\n") # and Mass\n")
    prt.prt_function(fp, f"Level II CP in Level I Units{' ':>22}size {cp_lvl_2_size:5.3e}  \n")   #{' ':>19}mass {cp_lvl_2_mass:5.3e}\n")
    prt.prt_function(fp, f"Level II CP In Level I Units{' ':>13}count by size {count_of_lvl_1_in_lvl_2_by_size:5.3e}  \n")   #{' ':>10}count by mass {count_of_lvl_1_in_lvl_2_by_mass:5.3e}\n")
    prt.prt_function(fp, "  \n")

    #calculated values
    #-----------------------------------------------------------------------------------------
    size1, mass1 = return_particle_size_mass("Series", item_size, item_mass)
    size2, mass2 = return_particle_size_mass("Series", item_size, item_mass)
    #tot_size_12 = size1 + size2
    #tot_mass_12 = mass1 + mass2

    #average the two sizes and masses
    tot_size_12_avg = (size1 + size2) / 2 
    #tot_mass_12_avg = (mass1 + mass2) / 2

    prt.prt_function(fp, "Calculated Size\n") # and Mass\n")
    prt.prt_function(fp, "Series Join - Sample Size of Two Level 1 Particles X and Y\n")
    prt.prt_function(fp, f"     Level I Particle X {' ':>26}size {size1:5.3e}  \n")   #{' ':>19}mass {mass1:5.3e}\n")
    prt.prt_function(fp, f"     Level I Particle Y {' ':>26}size {size2:5.3e}  \n")   #{' ':>19}mass {mass2:5.3e}\n")
    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, f"     Level I Particle X, Y Average** {' ':>13}size {tot_size_12_avg:5.3e}  \n")   #{' ':>19}mass {tot_mass_12:5.3e}\n")
    prt.prt_function(fp, "  \n")

    size3, mass3 = return_particle_size_mass("Quantitative", item_size, item_mass)
    size4, mass4 = return_particle_size_mass("Quantitative", item_size, item_mass)
    #tot_size_34 = size3 + size4
    #tot_mass_34 = mass3 + mass4

    # average th two sizes and massess
    tot_size_34_avg = (size3 + size4) / 2 
    tot_mass_34_avg = (mass3 + mass4) / 2

    prt.prt_function(fp, "Quantitative Join - Sample Size of Two Level 1 Particles X and Y\n")
    prt.prt_function(fp, f"     Level I Particle X {' ':>26}size {size3:5.3e}  \n")   #{' ':>19}mass {mass3:5.3e}\n")
    prt.prt_function(fp, f"     Level I Particle Y {' ':>26}size {size4:5.3e}  \n")   #{' ':>19}mass {mass4:5.3e}\n")
    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, f"     Level I Particle X, Y Average** {' ':>13}size {tot_size_34_avg:5.3e}  \n")   #{' ':>19}mass {tot_mass_34:5.3e}\n")
    prt.prt_function(fp, "  \n")

    """
    percent_split_series = 0.4       # 40% split to series
    percent_split_quant  = 0.6       # 60% split to quantitative

    count_size_2_series = count_of_lvl_1_in_lvl_2_by_size * percent_split_series
    count_mass_2_series = count_of_lvl_1_in_lvl_2_by_mass * percent_split_series

    count_size_2_quant  = count_of_lvl_1_in_lvl_2_by_size * percent_split_quant
    count_mass_2_quant  = count_of_lvl_1_in_lvl_2_by_mass * percent_split_quant

    tot_series_by_size = tot_size_12 * count_size_2_series
    tot_series_by_mass = tot_mass_12 * count_mass_2_series

    tot_quant_by_size  = tot_size_34 * count_size_2_quant
    tot_quant_by_mass  = tot_mass_34 * count_mass_2_quant

    prt.prt_function(fp, f"Total Level II Series Prtcl at {percent_split_series*100:.0f}% split{' ':>7}by size {tot_series_by_size:5.3e}{' ':>16}by mass {tot_series_by_mass:5.3e}\n")
    prt.prt_function(fp, f"Total Level II Quant. Prtcl at {percent_split_quant*100:.0f}% split {' ':>6}by size {tot_quant_by_size:5.3e}{' ':>16}by mass {tot_quant_by_mass:5.3e}\n")
    prt.prt_function(fp, f"{' ':>55}{'---------'}{' ':>24}{'---------'}\n")

    tot_lvl_2_s = tot_series_by_size + tot_quant_by_size
    tot_lvl_2_q = tot_series_by_mass + tot_quant_by_mass
    prt.prt_function(fp, f"Total Level II {' ':>32}by size {tot_lvl_2_s:5.3e}{' ':>16}by mass {tot_lvl_2_q:5.3e}\n")

    #now summarize inicatives
    f_size_count = item_s_size * count_of_lvl_1_in_lvl_2_by_size
    f_mass_count = item_m_mass * count_of_lvl_1_in_lvl_2_by_mass

    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "Itemized Details\n")
    prt.prt_function(fp, f"Count {{f}} in Level II:{' ':>33}{f_size_count:5.3e}{' ':>23}{f_mass_count:5.3e}\n")
    """

    prt.prt_function(fp, "** Will carry these Individual values, for  series and quantitative particles, to  \n")
    prt.prt_function(fp, "   Level III where they will be applied as groups. \n")
    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")
    
    #old code commented out with above
    #item_pass_list.append(ri.PassItems('Level II', tot_lvl_2_s, tot_lvl_2_q))
    #item_pass_list.append(ri.PassItems('Level II Counts', f_size_count, f_mass_count))

    #new code to compliment remaining code
    item_pass_list.append(ri.PassItems('Level II 12SAM', tot_size_12_avg, 0 )) #tot_mass_12_avg))
    item_pass_list.append(ri.PassItems('Level II 34SAM', tot_size_34_avg, 0 )) #tot_mass_34_avg))

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
        mass = 0 #random.uniform(init_mass * 0.3, init_mass * 0.4)
    else:
        #Quantitative
        size = random.uniform(init_size * 0.8, init_size * 1.0)
        mass = 0 #random.uniform(init_mass * 0.8, init_mass * 1.0)

    return(size, mass)
