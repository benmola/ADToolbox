import json
import numpy as np
from ADToolBox import Reaction_Toolkit, Metabolite
from collections import Counter as Counter
Base_Parameters = {"R": 0.083145,
                   "T_base": 298.15,
                   "P_atm": 1.013,
                   "T_op": 308.15,
                   "V_liq": 3400,
                   "V_gas": 300,
                   "pH_UL_ac": 7,
                   "pH_LL_ac": 6,
                   "pH_UL_aa": 5.5,
                   "pH_LL_aa": 4,
                   "pH_UL_h2": 6,
                   "pH_LL_h2": 5,
                   "pH_UL_pro":  5.5,
                   "pH_LL_pro":  4,
                   "pH_UL_bu":  5.5,
                   "pH_LL_bu":  4,
                   "pH_UL_va":  5.5,
                   "pH_LL_va":  4,
                   'q_in': 170
                   }


Species = [
    "S_su",
    "S_aa",
    "S_fa",
    "S_va",
    "S_bu",
    "S_pro",
    "S_et",
    "S_lac",
    "S_cap",
    "S_ac",
    "S_h2",
    "S_ch4",
    "S_IC",
    "S_IN",
    "S_I",
    "TSS",
    "TDS",
    "X_ch",
    "X_pr",
    "X_li",
    "X_su",
    "X_aa",
    "X_ac_et",
    "X_ac_lac",
    "X_fa",
    "X_VFA_deg",
    "X_et",
    "X_lac",
    "X_chain_et",
    "X_chain_lac",
    "X_Me_ac",
    "X_Me_CO2",
    "X_I",
    "S_cation",
    "S_anion",
    "S_H_ion",
    "S_va_ion",
    "S_bu_ion",
    "S_pro_ion",
    "S_cap_ion",
    "S_lac_ion",
    "S_ac_ion",
    "S_hco3_ion",
    "S_co2",
    "S_nh3",
    "S_nh4_ion",
    "S_gas_h2",
    "S_gas_ch4",
    "S_gas_co2",
]

Reactions = [
    'TSS_Disintegration',
    'TDS_Disintegration',
    'Hydrolysis carbohydrates',
    'Hydrolysis proteins',
    'Hydrolysis lipids',
    'Uptake of sugars',
    'Uptake of amino acids',
    'Uptake of LCFA',
    'Uptake of acetate_et',
    'Uptake of acetate_lac',
    'Uptake of propionate_et',
    'Uptake of propionate_lac',
    'Uptake of butyrate_et',
    'Uptake of butyrate_lac',
    'Uptake of valerate',
    'Uptake of caproate',
    'Methanogenessis from acetate and h2',
    'Methanogenessis from CO2 and h2',
    'Uptake of ethanol',
    'Uptake of lactate',
    'Decay of Xsu',
    'Decay of Xaa',
    'Decay of Xfa',
    'Decay of X_ac_et',
    'Decay of X_ac_lac',
    'Decay of Xpro',
    'Decay of X_chain_et',
    'Decay of X_chain_lac',
    "Decay of X_VFA_deg",
    'Decay of X_Me_ac',
    'Decay of X_Me_CO2',
    'Decay of Xet',
    'Decay of Xlac',
    'Acid Base Equilibrium (Va)',
    'Acid Base Equilibrium (Bu)',
    'Acid Base Equilibrium (Pro)',
    'Acid Base Equilibrium (Cap)',
    'Acid Base Equilibrium (Lac)',
    'Acid Base Equilibrium (Ac)',
    'Acid Base Equilibrium (CO2)',
    'Acid Base Equilibrium (In)',
    'Gas Transfer H2',
    'Gas Transfer CH4',
    'Gas Transfer CO2'
]


# USE the folowing template to find C_x
# SEED_DB = Reaction_Toolkit("./Database/compounds.json",
#                            "./Database/reactions.json")

# x_Seed = SEED_DB.Instantiate_Metabs("cpd01024")


# C_et = Counter(x_Seed.Dict["smiles"])[
#     "C"]/(x_Seed.Dict["mass"]*x_Seed.COD)


Model_Parameters = {
    "f_sI_TDS": 0.7,
    "f_xI_TSS":  0.8,
    "f_ch_TSS":  0.05,
    "f_ch_TDS":  0.1,
    "f_pr_TSS":  0.05,
    "f_pr_TDS":  0.1,
    "f_li_TSS":  0.1,
    "f_li_TDS":  0.1,
    "N_xc":  0.0376 / 14,
    "N_I": 0.06 / 14,
    "N_aa": 0.007,
    "C_xc": 0.02786,
    "C_sI": 0.03,
    "C_ch": 0.0313,
    "C_pr": 0.03,
    "C_li": 0.022,
    "C_xI": 0.03,
    "C_su": 0.0313,
    "C_et": 0.0208,
    "C_lac": 0.0340,
    "C_aa": 0.03,
    "f_fa_li": 0.95,
    "C_fa": 0.0217,



    "f_h2_su":  0.19,



    "f_pro_su":  0.1,
    'f_et_su':  0.1,
    'f_lac_su':  0.1,
    "f_ac_su":  0.6,

    "N_bac":  0.08 / 14,
    "C_bu":  0.025,
    "C_pro":  0.0268,
    "C_ac":  0.0313,
    "C_bac":  0.0313,
    "Y_su":  0.1,
    'K_I_h2_ox':3.5 * 10 ** -6,

    "f_h2_aa":  0.06,
    "f_va_aa":  0.1,
    "f_bu_aa":  0.1,
    "f_pro_aa":  0.05,
    "f_ac_aa":  0.1,
    'f_et_aa': 0.05,
    'f_lac_aa': 0.05,
    'f_h2_fa': 0.05,
    'Y_ac_et': 0.1,
    'f_et_ac': -1,
    'f_bu_ac': 0.1,
    'Y_ac_lac': 0.1,
    'f_lac_ac': -1,
    'f_h2_ac': 0.1,
    'Y_ac_et_ox':0.8,
    'Y_pro_lac_ox':0.4,


    'Y_pro_et': 0.1,
    'f_et_pro': -1,
    'f_va_pro': 0.1,
    'Y_pro_lac': 0.1,
    'f_lac_pro': -1,
    'f_h2_pro': 0.1,
    'Y_chain_et_pro': 0.2,
    'Y_chain_lac_pro': 0.2,
    'Y_bu_et': 0.4,
    'f_et_bu': -0.1,
    'f_cap_bu': 0.5,
    "C_cap": 0.0241,
    'Y_bu_lac': 0.1,
    'f_lac_bu': -0.1,
    'f_h2_bu': 0.01,
    'Y_va': 0.2,
    'Y_cap': 0.1,
    'Y_h2_ac': 0.05,
    'Y_h2_CO2': 0.05,
    'f_ac_h2': -1,
    'Y_Me_ac': 0.05,
    'Y_Me_CO2': 0.05,
    'C_ch4': 0.0156,
    'Y_Me_h2': 0.05,
    "C_va":  0.024,
    "Y_aa":  0.08,
    "Y_fa":  0.06,
    "Y_c4":  0.06,
    "Y_pro":  0.04,
    "C_ch4":  0.0156,
    "Y_ac":  0.05,
    "Y_h2":  0.06,
    "k_dis_TSS":  0.01,
    "k_dis_TDS":  0.2,
    "k_hyd_ch":  5,
    "k_hyd_pr":  5,
    "k_hyd_li":  5,
    "K_S_IN":  10 ** -4,
    "k_m_su":  30,
    "K_S_su":  0.5,
    "pH_UL_aa":  5.5,
    "pH_LL_aa":  4,


    "k_m_aa":  50,
    "K_S_aa":  0.3,
    "k_m_fa":  6,
    "K_S_fa":  0.4,
    "K_I_h2_fa":  5 * 10 ** -6,



    'k_m_bu': 0.20,
    'K_S_bu': 0.2,
    'k_m_va': 20,
    'K_S_va': 0.2,
    'k_m_cap': 0.20,
    'K_S_cap': 0.2,
    "K_I_h2_c4":  10 ** -5,
    "k_m_pro":  0.13,
    "K_S_pro":  0.1,
    "k_m_et":  0.13,
    "K_S_et":  0.1,
    "k_m_lac":  0.13,
    "K_S_lac":  0.1,
    "K_I_h2_pro":  3.5 * 10 ** -6,
    "k_m_ac":  0.8,
    "K_S_ac":  0.15,
    "K_I_nh3":  0.0018,
    'k_m_h2_Me_ac': 35,
    'K_S_h2_Me_ac': 7 * 10 ** -6,
    'K_S_ac_Me': 0.1,
    'k_m_h2_Me_CO2': 35,
    'K_S_h2_Me_CO2': 7 * 10 ** -6,
    'K_S_CO2_Me': 0.1,
    "k_dec_X_su":  0.0002,
    "k_dec_X_aa":  0.0002,
    "k_dec_X_fa":  0.0002,
    "k_dec_X_c4":  0.0002,
    "k_dec_X_pro":  0.0002,
    "k_dec_X_ac":  0.0002,
    "k_dec_X_h2":  0.0002,
    "N_xc":  0.0376 / 14,
    "N_I":  0.06 / 14,
    "N_aa":  0.007,
    "C_xc":  0.02786,
    "C_sI":  0.03,
    "C_ch":  0.0313,
    "C_pr":  0.03,
    "C_li":  0.022,
    "C_xI":  0.03,
    "C_su":  0.0313,
    "C_aa":  0.03,
    "f_fa_li":  0.95,
    "C_fa":  0.0217,
    "f_h2_su":  0.19,
    "f_bu_su":  0.13,
    "f_pro_su":  0.27,
    "f_ac_su":  0.41,
    "N_bac":  0.08 / 14,
    "C_bu":  0.025,
    "C_pro":  0.0268,
    "C_ac":  0.0313,
    "C_bac":  0.0313,
    "Y_su":  0.1,
    "f_h2_aa":  0.06,
    "f_va_aa":  0.23,
    "f_bu_aa":  0.26,
    "f_pro_aa":  0.05,
    "f_ac_aa":  0.20,
    'f_pro_fa': 0.1,
    'f_et_fa': 0.01,
    'f_lac_fa': 0.01,
    'f_ac_fa': 0.1,
    "C_va":  0.024,
    "Y_aa":  0.08,
    "Y_fa":  0.06,
    "Y_c4":  0.06,
    "Y_pro":  0.04,
    "C_ch4":  0.0156,
    "Y_ac":  0.05,
    "Y_h2":  0.06,
    "k_dis":  0.5,
    "K_S_IN":  10 ** -4,
    "k_m_su":  30,
    "K_S_su":  0.5,
    'K_S_pro_lac': 0.1,
    'K_S_ac_et': 0.1,
    "k_m_aa":  50,
    "K_S_aa":  0.3,
    "k_m_fa":  6,
    "K_S_fa":  0.4,
    "K_I_h2_fa":  5 * 10 ** -6,
    "k_m_pr":  13,
    "K_S_c4":  0.2,
    "K_I_h2_c4":  10 ** -5,
    "k_m_pro":  0.13,
    "K_S_pro":  0.1,
    "K_I_h2_pro":  3.5 * 10 ** -6,
    "k_m_ac":  8,
    "K_S_ac":  0.15,
    "K_I_nh3":  0.0018,
    "Q_ad": 1000.0,
    "k_m_h2":  35,
    "K_S_h2":  7 * 10 ** -6,
    "k_dec_X_su":  0.02,
    'k_dec_X_chain_et': 0.001,
    'k_dec_X_chain_lac': 0.001,
    'k_dec_X_VFA_deg': 0.001,
    'k_dec_X_Me_ac': 0.001,
    'k_dec_X_Me_CO2': 0.001,
    'k_dec_X_et': 0.001,
    'k_dec_X_lac': 0.001,
    "k_dec_X_aa":  0.02,
    "k_dec_X_fa":  0.02,
    "k_dec_X_c4":  0.02,
    "k_dec_X_pro":  0.02,
    "k_dec_X_ac":  0.02,
    "k_dec_X_h2":  0.02,
    "K_w":  10 ** -14.0 * np.exp((55900 / (100 * Base_Parameters["R"])) * (1 / Base_Parameters["T_base"] - 1 / Base_Parameters["T_op"])),
    "K_a_va":  10 ** -4.86,
    "K_a_bu":  10 ** -4.82,
    "K_a_pro":  10 ** -4.88,
    'K_a_cap': 10 ** -4.88,
    "K_a_ac":  10 ** -4.76,
    'K_a_lac': 10 ** -4.76,
    "K_a_co2":  10 ** -6.35 * np.exp((7646 / (100 * Base_Parameters["R"])) * (1 / Base_Parameters["T_base"] - 1 / Base_Parameters["T_op"])),
    "K_a_IN":  10 ** -9.25 * np.exp((51965 / (100 * Base_Parameters["R"])) * (1 / Base_Parameters["T_base"] - 1 / Base_Parameters["T_op"])),
    "k_A_B_va":  10 ** 10,
    "k_A_B_bu":  10 ** 10,
    'k_A_B_lac': 10 ** 10,
    'k_A_B_cap': 10 ** 10,
    "k_A_B_pro":  10 ** 10,
    "k_A_B_ac":  10 ** 10,
    "k_A_B_co2":  10 ** 10,
    "k_A_B_IN":  10 ** 10,
    "p_gas_h2o":  0.0313 * np.exp(5290 * (1 / Base_Parameters["T_base"] - 1 / Base_Parameters["T_op"])),
    "k_p": 5 * 10 ** 4,
    "k_L_a":  200.0,
    "K_H_co2":  0.035 * np.exp((-19410 / (100 * Base_Parameters["R"])) * (1 / Base_Parameters["T_base"] - 1 / Base_Parameters["T_op"])),
    "K_H_ch4":  0.0014 * np.exp((-14240 / (100 * Base_Parameters["R"])) * (1 / 1 / Base_Parameters["T_base"] - 1 / Base_Parameters["T_op"])),
    "K_H_h2":  7.8 * 10 ** -4 * np.exp(-4180 / (100 * Base_Parameters["R"]) * (1 / 1 / Base_Parameters["T_base"] - 1 / Base_Parameters["T_op"])),
    "V_ad": Base_Parameters["V_liq"] + Base_Parameters["V_gas"],
    "K_pH_aa": (10 ** (-1 * (Base_Parameters["pH_LL_aa"] + Base_Parameters["pH_UL_aa"]) / 2.0)),
    "nn_aa":  (3.0 / (Base_Parameters["pH_UL_aa"] - Base_Parameters["pH_LL_aa"])),
    "K_pH_ac":  (10 ** (-1 * (Base_Parameters["pH_LL_ac"] + Base_Parameters["pH_UL_ac"]) / 2.0)),
    "n_ac":  (3.0 / (Base_Parameters["pH_UL_ac"] - Base_Parameters["pH_LL_ac"])),

    "K_pH_h2":  (10 ** (-1 * (Base_Parameters["pH_LL_h2"] + Base_Parameters["pH_UL_h2"]) / 2.0)),
    "n_h2":  (3.0 / (Base_Parameters["pH_UL_h2"] - Base_Parameters["pH_LL_h2"])),

    "K_pH_pro":  (10 ** (-1 * (Base_Parameters["pH_LL_pro"] + Base_Parameters["pH_UL_pro"]) / 2.0)),
    "n_pro":  (3.0 / (Base_Parameters["pH_UL_pro"] - Base_Parameters["pH_LL_pro"])),

    "K_pH_bu":  (10 ** (-1 * (Base_Parameters["pH_LL_bu"] + Base_Parameters["pH_UL_bu"]) / 2.0)),
    "n_bu":  (3.0 / (Base_Parameters["pH_UL_bu"] - Base_Parameters["pH_LL_bu"])),

    "K_pH_va":  (10 ** (-1 * (Base_Parameters["pH_LL_va"] + Base_Parameters["pH_UL_va"]) / 2.0)),
    "n_va":  (3.0 / (Base_Parameters["pH_UL_va"] - Base_Parameters["pH_LL_va"])),

    "K_pH_cap":  (10 ** (-1 * (Base_Parameters["pH_LL_bu"] + Base_Parameters["pH_UL_bu"]) / 2.0)),
    "n_cap":  (3.0 / (Base_Parameters["pH_UL_bu"] - Base_Parameters["pH_LL_bu"])),

}

Inlet_Conditions = {"S_su_in": 0.01,
                    "S_aa_in": 0.001,
                    "S_fa_in": 0.001,
                    "S_va_in": 0.001,
                    "S_bu_in": 0.001,
                    'S_et_in': 0.000,
                    "S_lac_in": 0.000,
                    "S_pro_in": 0.001,
                    "S_cap_in": 0.000,
                    "TSS_in": 12.0,
                    "TDS_in": 3.0,
                    "S_ac_in": 0.001,
                    'X_chain_lac_in': 0.01,
                    "S_h2_in": 10 ** -8,
                    "S_ch4_in": 10 ** -5,
                    "S_IC_in": 0.04,
                    "S_IN_in": 0.01,
                    "S_I_in": 0.02,
                    "X_xc_in": 2.0,
                    'X_ac_et_in': 1.0,
                    'X_Me_ac_in': 0.1,
                    'X_Me_CO2_in': 0.1,
                    'S_cap_ion_in': 0.001,
                    "S_lac_ion_in": 0.000,
                    'X_et_in': 0.01,
                    'X_lac_in': 0.01,
                    'X_chain_et_in': 0.01,
                    "X_ac_et_in": 0.001,
                    "X_ac_lac_in": 0.001,
                    "X_ch_in": 5.0,
                    "X_pr_in": 20.0,
                    'X_ac_lac_in': 0.01,
                    'X_VFA_deg_in': 0.01,
                    "X_li_in": 5.0,
                    "X_su_in": 0.0,
                    "X_aa_in": 0.01,
                    "X_fa_in": 0.01,
                    "X_c4_in": 0.01,
                    "X_pro_in": 0.01,
                    "X_ac_in": 0.01,
                    "X_h2_in": 0.01,
                    "X_I_in": 25.0,
                    "S_cation_in": 0.04,
                    "S_anion_in": 0.02,
                    "S_H_ion_in": 0.00000003423,
                    "S_va_ion_in": 0,
                    "S_bu_ion_in": 0.0,
                    "S_pro_ion_in": 0.0,
                    "S_ac_ion_in": 0,
                    "S_hco3_ion_in": 0,
                    "S_nh3_in": 0.0,
                    "S_gas_h2_in": 0,
                    "S_gas_ch4_in": 0,
                    "S_gas_co2_in": 0.0,
                    "S_nh4_ion_in":  0,
                    "S_co2_in":  0
                    }


Initial_Conditions = {"S_su": 0.1,
                      "S_aa": 0.01,
                      "S_fa": 0.01,
                      "S_va": 0.001,
                      "S_bu": 0.001,
                      'S_et': 0.000,
                      "S_lac": 0.000,
                      "S_pro": 0.001,
                      "S_cap": 0.000,
                      "TSS": 12.0,
                      "TDS": 3.0,
                      "S_ac": 0.001,
                      'X_chain_lac': 0.01,
                      "S_h2": 10 ** -8,
                      "S_ch4": 10 ** -5,
                      "S_IC": 0.04,
                      "S_IN": 0.01,
                      "S_I": 0.02,
                      "X_xc": 2.0,
                      'X_ac_et': 1.0,
                      'X_Me_ac': 0.1,
                      'X_Me_CO2': 0.1,
                      'S_cap_ion': 0.001,
                      "S_lac_ion": 0.000,
                      'X_et': 0.01,
                      'X_lac': 0.01,
                      'X_chain_et': 0.01,
                      "X_ch": 5.0,
                      "X_pr": 20.0,
                      'X_ac_lac': 0.01,
                      'X_VFA_deg': 0.01,
                      "X_ac_et": 0.001,
                      "X_ac_lac": 0.001,
                      "X_li": 5.0,
                      "X_su": 0.0,
                      "X_aa": 0.01,
                      "X_fa": 0.01,
                      "X_c4": 0.01,
                      "X_pro": 0.01,
                      "X_ac": 0.01,
                      "X_h2": 0.01,
                      "X_I": 25.0,
                      "S_cation": 0.04,
                      "S_anion": 0.02,
                      "S_H_ion": 0.00000003423,
                      "S_va_ion": 0,
                      "S_bu_ion": 0.0,
                      "S_pro_ion": 0.0,
                      "S_ac_ion": 0,
                      "S_hco3_ion": 0,
                      "S_nh3": 0.0,
                      "S_gas_h2": 0,
                      "S_gas_ch4": 0,
                      "S_gas_co2": 0.0,
                      "S_nh4_ion":  0,
                      "S_co2":  0
                      }
if __name__ == "__main__":
    with open('Modified_ADM_Base_Parameters.json', 'w') as fp:
        json.dump(Base_Parameters, fp)
    with open('Modified_ADM_Inlet_Conditions.json', 'w') as fp:
        json.dump(Inlet_Conditions, fp)
    with open('Modified_ADM_Initial_Conditions.json', 'w') as fp:
        json.dump(Initial_Conditions, fp)
    with open('Modified_ADM_Reactions.json', 'w') as fp:
        json.dump(Reactions, fp)
    with open('Modified_ADM_Species.json', 'w') as fp:
        json.dump(Species, fp)
    with open('Modified_ADM_Model_Parameters.json', 'w') as fp:
        json.dump(Model_Parameters, fp)
    
