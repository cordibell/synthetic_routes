# aliphatic compounds

import random

# adjacency list of all the connections

aliphatic_compounds = {
    "Alkane": {"Haloalkane" : "Halogen/UV light"},
     "Alkene": {"Alkane" : "H2/Ni", "Haloalkane" : "Hydrogen Halide", "Alcohol" : "Steam/H3PO4"},
     "Haloalkane" : {"Nitrile" : "Ethanolic HCN", "Amine" : "Ethanolic NH3", "Alcohol" : "NaOH"},
     "Alcohol" : {"Haloalkane" : "Sodium Halide/ H2SO4", "Alkene" : "H3PO4", "Ketone" : "K2Cr2O7/H2SO4/Reflux (2ndary)", "Aldehyde" : "K2Cr2O7/H2SO4/Distillation", "Carboxylic acid" : "K2Cr2O7/H2SO4/Reflux (primary)", "Ester" : "Carboxylic acid/H2SO4 or acid anhydride"},
     "Aldehyde" : {"Alcohol" : "NaBH4", "Hydroxynitrilie" : "HCN/Acid catalyst", "Carboxylic acid" : "K2Cr2O7/H2SO4/Reflux"},
     "Carboxylic acid" : {"Ester" : "Alcohol/H2SO4", "Acyl Chloride" : "SOCl2"},
     "Ester" : {"Carboxylate" : "Base hydrolysis/heat", "Carboxylic acid" : "Acid hydrolysis/heat"},
     "Carboxylate" : {},
     "Acyl Chloride" : {"Ester" : "Alcohol", "Carboxylic acid" : "H2O", "Primary Amide" : "NH3", "Secondary Amide" : "Primary amine"},
     "Primary amide" : {},
     "Secondary amide" : {},
     "Nitrile" : {"Amine" : "H2/Ni", "Carboxylic acid" : "Acid hydrolysis/heat"},
     "Amine" : {},
     "Ketone" : {"Alcohol" : "NaBH4", "Hydroxynitrile" : "HCN"},
     "Hydroxynitrile" : {"Carboxylic acid" : "Acid hydrolysis/heat", "Amine" : "H2/Ni"}
    }

def how_many_steps():
    num_steps = int(input("How many steps would you like there to be?"))
    