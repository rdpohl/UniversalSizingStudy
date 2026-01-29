'''
Author:   Richard D. Pohl
Date:     April, 2024
Summary:  Build and Report on a Level Three Composite Particle
'''

import refitems as ri
import prtfunction as prt

def level_3_size_and_mass(item_refs_list, item_pass_list, fp):
    """Version 1.0.0: Initial Release"""

    item_number_12_s = ri.find_record(item_pass_list, 'Level II 12SAM')
    item_size_12_ss  = item_pass_list[item_number_12_s].size
    #item_mass_12_sm  = item_pass_list[item_number_12_s].mass

    item_number_34_q = ri.find_record(item_pass_list, 'Level II 34SAM')
    item_size_34_qs  = item_pass_list[item_number_34_q].size
    #item_mass_34_qm  = item_pass_list[item_number_34_q].mass

    #prt.prt_function(fp, "  \n")
    #prt.prt_function(fp, "  \n")

    hydrogen:  int = 6
    sun:       int = 2
    galaxy:    int = 0

    level_three: int = sun
    
    #now project size/mass of Level II Composite Particle
    #get drill-down factor as size/mass of hyrdrogen to galaxy size/mass
    cp_3_size_factor = item_refs_list[level_three].size / item_refs_list[galaxy].size
    #cp_3_mass_factor = item_refs_list[level_three].mass / item_refs_list[galaxy].mass

    #use the factor and drill down from hydrogen to determine {f} size/mass
    cp_lvl_3_size = item_refs_list[hydrogen].size * cp_3_size_factor
    #cp_lvl_3_mass = item_refs_list[hydrogen].mass * cp_3_mass_factor

    count_of_lvl_2_in_lvl_3_by_size = cp_lvl_3_size /  (item_size_12_ss + item_size_34_qs)
    #count_of_lvl_2_in_lvl_3_by_mass = cp_lvl_3_mass /  (item_mass_12_sm + item_mass_34_qm)

    prtstr = "Level III Composite Particle Summary of Size\n" # and Mass\n"
    prt.prt_function(fp, prtstr)
    prt.prt_function(fp, "Projections of Size\n")
    prt.prt_function(fp, f"Level III{' ':>41}size {cp_lvl_3_size:5.3e}  \n")   #{' ':>19}mass {cp_lvl_3_mass:5.3e}\n")
    prt.prt_function(fp, f"Level III CP In Level II Units{' ':>19}count {count_of_lvl_2_in_lvl_3_by_size:5.3e} A \n")   #{' ':>10}count by mass {count_of_lvl_2_in_lvl_3_by_mass:5.3e}\n")
    prt.prt_function(fp, "  \n")
    
    #now process calculated values
    prt.prt_function(fp, "Calculated Size \n")
    prt.prt_function(fp, f"Individual Sizes for Level II: {' ':>17}Series {item_size_12_ss:5.3e} Ba{' ':>5}Quantitative {item_size_34_qs:5.3e} Bb\n")
    
    #avg_series_size = (item_size_12_ss + item_size_34_qs) / 2
    #count_of_l2_in_l3_by_series_size = cp_lvl_3_size / item_size_12_ss
        
    #avg_quant_mass  = (item_mass_12_sm + item_mass_34_qm) / 2
    #count_of_l2_in_l3_by_quant_size = cp_lvl_3_size /  item_size_34_qs

    #prt.prt_function(fp, f"Counts of Level II Units: {' ':>22}Series {count_of_l2_in_l3_by_series_size:5.3e}{' ':>7}Quantitative {count_of_l2_in_l3_by_quant_size:5.3e}\n")
    prt.prt_function(fp, "  \n")
    
    percent_split_series_eff = 0.3       # Percent split to series particles
    percent_split_quant_eff  = 0.7       # Percent split to quantitative particles

    percent_split_series_ineff = 0.05       # Percent split to series particles
    percent_split_quant_ineff  = 0.95       # Percent split to quantitative particles

    count_of_l2_in_l3_by_series_size_pct_eff = count_of_lvl_2_in_lvl_3_by_size #* percent_split_series_eff
    count_of_l2_in_l3_by_quant_size_pct_eff  = count_of_lvl_2_in_lvl_3_by_size #* percent_split_quant_eff
    size_of_l2_in_l3_by_series_size_pct_eff  = item_size_12_ss  #count_of_l2_in_l3_by_series_size_pct_eff * 
    size_of_l2_in_l3_by_quant_size_pct_eff   = item_size_34_qs  #count_of_l2_in_l3_by_quant_size_pct_eff  * 
    prt.prt_function(fp, f"Percent Splits Effective:{' ':>29}Series {percent_split_series_eff * 100:.0f}% C{' ':>12}Quantitative {percent_split_quant_eff * 100:.0f}% D\n")
    #prt.prt_function(fp, f"Counts of Level III Units by Pct Effective:{' ':>5}Series {count_of_l2_in_l3_by_series_size_pct_eff:5.3e}{' ':>11}Quantitative {count_of_l2_in_l3_by_quant_size_pct_eff:5.3e}\n")
    #prt.prt_function(fp, f"Size of Level III in L-II Units Effective:{' ':>6}Series {size_of_l2_in_l3_by_series_size_pct_eff:5.3e}{' ':>11}Quantitative {size_of_l2_in_l3_by_quant_size_pct_eff:5.3e}\n")
    tempa = count_of_lvl_2_in_lvl_3_by_size * item_size_12_ss * percent_split_series_eff
    tempb = count_of_lvl_2_in_lvl_3_by_size * item_size_34_qs * percent_split_quant_eff
    tempc = tempa + tempb
    prt.prt_function(fp, f"Total Size LIII in LII Units Effective:{' ':>7}(A*Ba*C) {tempa:5.3e} Ta{' ':>9}(A*Bb*D) {tempb:5.3e} Tb\n")
    prt.prt_function(fp, f"Effective Talley:{' ':>60}(Ta+Tb) {tempc:5.3e}\n")

    prt.prt_function(fp, "  \n")

    count_of_l2_in_l3_by_series_size_pct_ineff = count_of_lvl_2_in_lvl_3_by_size  #* percent_split_series_ineff
    count_of_l2_in_l3_by_quant_size_pct_ineff  = count_of_lvl_2_in_lvl_3_by_size  #* percent_split_quant_ineff
    size_of_l2_in_l3_by_series_size_pct_ineff  = item_size_12_ss  #count_of_l2_in_l3_by_series_size_pct_ineff * 
    size_of_l2_in_l3_by_quant_size_pct_ineff   = item_size_34_qs  #count_of_l2_in_l3_by_quant_size_pct_ineff  * 
    prt.prt_function(fp, f"Percent Splits Ineffective:{' ':>28}Series {percent_split_series_ineff * 100:.0f}% E{' ':>12}Quantitative {percent_split_quant_ineff * 100:.0f}% F\n")
    #prt.prt_function(fp, f"Counts of Level III Units by Pct InEffective:{' ':>3}Series {count_of_l2_in_l3_by_series_size_pct_ineff:5.3e}{' ':>11}Quantitative {count_of_l2_in_l3_by_quant_size_pct_ineff:5.3e}\n")
    #prt.prt_function(fp, f"Size of Level III in L-II Units Ineffective:{' ':>4}Series {size_of_l2_in_l3_by_series_size_pct_ineff:5.3e}{' ':>11}Quantitative {size_of_l2_in_l3_by_quant_size_pct_ineff:5.3e}\n")
    tempm = count_of_lvl_2_in_lvl_3_by_size * item_size_12_ss * percent_split_series_ineff
    tempn = count_of_lvl_2_in_lvl_3_by_size * item_size_34_qs * percent_split_quant_ineff
    tempo = tempm + tempn
    prt.prt_function(fp, f"Total Size of LIII in LII Units InEffective:{' ':>2}(A*Ba*E) {tempm:5.3e} Tc{' ':>9}(A*Bb*F) {tempn:5.3e} Td\n")
    prt.prt_function(fp, f"Effective Talley:{' ':>60}(Tc+Td) {tempo:5.3e}\n")

    
    #prt.prt_function(fp, "  \n")
    #prt.prt_function(fp, "  \n")
    #prt.prt_function(fp, "*  User Configurable  \n")    
    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")

    """
    item_pass_list.append(ri.PassItems('Level III Effective', size_of_lvl_2_in_lvl_3_by_series_size_pct_eff + 
                                                              size_of_lvl_2_in_lvl_3_by_quant_size_pct_eff, 
                                                              count_of_lvl_2_in_lvl_3_by_series_size_pct_eff + 
                                                              count_of_lvl_2_in_lvl_3_by_quant_size_pct_eff)) 
    
    item_pass_list.append(ri.PassItems('Level III Ineffective',size_of_lvl_2_in_lvl_3_by_series_size_pct_ineff + 
                                                               size_of_lvl_2_in_lvl_3_by_quant_size_pct_ineff, 
                                                               count_of_lvl_2_in_lvl_3_by_series_size_pct_ineff + 
                                                               count_of_lvl_2_in_lvl_3_by_quant_size_pct_ineff))
    
    item_pass_list.append(ri.PassItems('Level III Counts', 0 , 0)) 
    """

    """
    #now process calculated values
    lvl_3_size = count_of_lvl_2_in_lvl_3_by_size * item_size
    lvl_3_mass = count_of_lvl_2_in_lvl_3_by_mass * item_mass

    find_number = ri.find_record(item_pass_list, 'Level II')
    find_size   = item_pass_list[find_number].size
    find_mass   = item_pass_list[find_number].mass
    lvl_3_effect_size   = lvl_3_size + (count_of_lvl_2_in_lvl_3_by_size * find_size)
    lvl_3_effect_mass   = lvl_3_mass + (count_of_lvl_2_in_lvl_3_by_mass * find_mass)

    lvl_3_in_effect_size = lvl_3_size * 1.05   #?? 5%
    lvl_3_in_effect_mass = lvl_3_mass * 1.05

    prt.prt_function(fp, "Calculated Size and Mass\n")
    prt.prt_function(fp, f"Total Level III Effective Conductor{' ':>12}by size {lvl_3_effect_size:5.3e}{' ':>16}by mass {lvl_3_effect_mass:5.3e}\n")
    prt.prt_function(fp, f"Total Level III Ineffective Conductor{' ':10}by size {lvl_3_in_effect_size:5.3e}{' ':>16}by mass {lvl_3_in_effect_mass:5.3e}\n")
    prt.prt_function(fp, f"{' ':>55}{'---------'}{' ':>24}{'---------'}\n")

    avg_lvl_3_size = lvl_3_effect_size + lvl_3_in_effect_size
    avg_lvl_3_mass = lvl_3_effect_mass + lvl_3_in_effect_mass

    prt.prt_function(fp, f"Total Level III {' ':>23}Average by size {avg_lvl_3_size:5.3e}{' ':>16}by mass {avg_lvl_3_mass:5.3e}\n")

    #now summarize inicatives
    f_size_counta = item_s_sizea * count_of_lvl_2_in_lvl_3_by_size
    f_mass_counta = item_m_massa * count_of_lvl_2_in_lvl_3_by_mass

    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "Itemized Details\n")
    prt.prt_function(fp, f"Count {{f}} in Level III:{' ':>32}{f_size_counta:5.3e}{' ':>23}{f_mass_counta:5.3e}\n")

    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")
    """
    
    item_pass_list.append(ri.PassItems('Level III Effective', tempc, count_of_lvl_2_in_lvl_3_by_size))
    item_pass_list.append(ri.PassItems('Level III Ineffective', tempo, count_of_lvl_2_in_lvl_3_by_size))
    #item_pass_list.append(ri.PassItems('Level III Counts', f_size_counta, 0))
    

    return item_refs_list, item_pass_list
