'''
Author:   Richard D. Pohl
Date:     April, 2024
Summary:  Build and Report on a Level Three Composite Particle
'''

import refitems as ri
import prtfunction as prt
import readjson as rj

def level_3_size_and_mass(item_refs_list, item_pass_list, json_ptr, fp):
    """Version 1.0.0: Initial Release"""

    with open(json_ptr, "r") as f:
       reader = rj.JSONReader(json_ptr)
       if reader.read_json_file():
            # Access data using standard dictionary syntax or the helper method
            percent_split_series_eff   = reader.get_value(['levelthree','percent_split_series_eff'])
            percent_split_quant_eff    = reader.get_value(['levelthree','percent_split_quant_eff'])
            percent_split_series_ineff = reader.get_value(['levelthree','percent_split_series_ineff']) 
            percent_split_quant_ineff  = reader.get_value(['levelthree','percent_split_quant_ineff'])
            percent_eff_comp           = reader.get_value(['levelthree','percent_eff_comp']) 

    item_number_12_s = ri.find_record(item_pass_list, 'Level II 12SAM')
    item_size_12_ss  = item_pass_list[item_number_12_s].size
    
    item_number_34_q = ri.find_record(item_pass_list, 'Level II 34SAM')
    item_size_34_qs  = item_pass_list[item_number_34_q].size
    
    electron:  int = 8
    hydrogen:  int = 6
    sun:       int = 2
    solar_sys: int = 1
    galaxy:    int = 0

    level_three: int = sun
    
    #now project size of Level II Composite Particle
    #get drill-down factor as size of hyrdrogen to galaxy size
    cp_3_size_factor = item_refs_list[level_three].size / item_refs_list[galaxy].size
    
    #use the factor and drill down from hydrogen to determine {f} size
    cp_lvl_3_size = item_refs_list[hydrogen].size * cp_3_size_factor
    
    count_of_lvl_2_in_lvl_3_by_size = cp_lvl_3_size /  (item_size_12_ss + item_size_34_qs)
    
    prtstr = "Level III Composite Particle Summary of Size\n" 
    prt.prt_function(fp, prtstr)
    prt.prt_function(fp, "Projections of Size\n")
    prt.prt_function(fp, f"Level III{' ':>41}size {cp_lvl_3_size:5.3e}  \n")   
    prt.prt_function(fp, f"Level III CP In Level II Units{' ':>19}count {count_of_lvl_2_in_lvl_3_by_size:5.3e} A \n") 
    prt.prt_function(fp, "  \n")
    
    #now process calculated values
    prt.prt_function(fp, "Calculated Size \n")
    prt.prt_function(fp, f"Individual Sizes for Level II: {' ':>17}Series {item_size_12_ss:5.3e} Ba{' ':>5}Quantitative {item_size_34_qs:5.3e} Bb\n")
    
    prt.prt_function(fp, "  \n")
    
    count_of_l2_in_l3_by_series_size_pct_eff = count_of_lvl_2_in_lvl_3_by_size 
    count_of_l2_in_l3_by_quant_size_pct_eff  = count_of_lvl_2_in_lvl_3_by_size 
    size_of_l2_in_l3_by_series_size_pct_eff  = item_size_12_ss  
    size_of_l2_in_l3_by_quant_size_pct_eff   = item_size_34_qs  
    prt.prt_function(fp, f"Percent Splits Effective:{' ':>29}Series {percent_split_series_eff * 100:.0f}% C{' ':>12}Quantitative {percent_split_quant_eff * 100:.0f}% D\n")
    tempa = count_of_lvl_2_in_lvl_3_by_size * item_size_12_ss * percent_split_series_eff
    tempb = count_of_lvl_2_in_lvl_3_by_size * item_size_34_qs * percent_split_quant_eff
    tempc = tempa + tempb
    prt.prt_function(fp, f"Total Size LIII in LII Units Effective:{' ':>7}(A*Ba*C) {tempa:5.3e} Ta{' ':>9}(A*Bb*D) {tempb:5.3e} Tb\n")
    prt.prt_function(fp, f"Effective Talley:{' ':>60}(Ta+Tb) {tempc:5.3e} G\n")

    prt.prt_function(fp, "  \n")

    count_of_l2_in_l3_by_series_size_pct_ineff = count_of_lvl_2_in_lvl_3_by_size 
    count_of_l2_in_l3_by_quant_size_pct_ineff  = count_of_lvl_2_in_lvl_3_by_size 
    size_of_l2_in_l3_by_series_size_pct_ineff  = item_size_12_ss  
    size_of_l2_in_l3_by_quant_size_pct_ineff   = item_size_34_qs  
    prt.prt_function(fp, f"Percent Splits Ineffective:{' ':>28}Series {percent_split_series_ineff * 100:.0f}% E{' ':>12}Quantitative {percent_split_quant_ineff * 100:.0f}% F\n")
    tempm = count_of_lvl_2_in_lvl_3_by_size * item_size_12_ss * percent_split_series_ineff
    tempn = count_of_lvl_2_in_lvl_3_by_size * item_size_34_qs * percent_split_quant_ineff
    tempo = tempm + tempn
    prt.prt_function(fp, f"Total Size of LIII in LII Units InEffective:{' ':>2}(A*Ba*E) {tempm:5.3e} Tc{' ':>9}(A*Bb*F) {tempn:5.3e} Td\n")
    prt.prt_function(fp, f"Ineffective Talley:{' ':>58}(Tc+Td) {tempo:5.3e}\n")

    prt.prt_function(fp, "  \n")

    cp_comp_size        = (tempc * percent_eff_comp) * 2       #g * h * 2  (2 Ep per CmP)
    count_cp_comp_size  = cp_lvl_3_size / cp_comp_size

    prt.prt_function(fp, f"Percent Complementary Size Difference:{' ':>23}{percent_eff_comp * 100:.0f}% H{' ':>12}\n")
    prt.prt_function(fp, f"Total Size of Complementary Particle:{' ':>10}(G*H*2) {cp_comp_size:5.3e} Tz\n") 
    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")
    
    item_pass_list.append(ri.PassItems('Level III Effective', tempc, count_of_lvl_2_in_lvl_3_by_size))
    item_pass_list.append(ri.PassItems('Level III Ineffective', tempo, count_of_lvl_2_in_lvl_3_by_size))
    item_pass_list.append(ri.PassItems('Level III Comp', cp_comp_size, count_cp_comp_size))    

    return item_refs_list, item_pass_list
