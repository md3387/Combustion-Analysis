# Combustion-Analysis
A variety of Matlab or Python functions that are useful plug-ins for combustion analysis
Each function has a Matlab version and a Python version.

Functions:-----------------------------------------------------------------------------

ParseElementString -
  M. Hageman 11/2018
  Parse Element name strings to find the names and quantities of individual elements, 
  Handles chemical names w/o coefficients behind each element (Like in CH4 or N2O)
  Primary code taken verbatim from Fangjun Jiang on MATLAB Answers: 
      https://www.mathworks.com/matlabcentral/answers/13600-how-to-extract-info-from-a-chemical-formula
      Accessed 11/6/2018
  Inputs: str (Chemical name)
  Output:EleList (cell array of element names) NumList (array of element coefficients)

CHON_MW - 
  M. Hageman 11/2018
  Determines the molecular weight [kg/kmol] of a molecule from the molecular formula primarily for hydrocarbons.  \
  Elements that can be included in the molecule are: C (carbon) H (Hydrogen) O(Oxygen) N(Nitrogen) Ar(Argon) He(Helium)
  Inputs: SpeciesName  (example: 'CH4' or 'O2' etc.  Only CHON+Ar+He containing molecules will work)
  Outputs: MW  (molecular weight of the input species [kg/kmol or g/mol])
  Requires Subfunctions:
      1) ParseElementString.m

FindStoich -
  M Hageman 11/2018
  Determines the stoichiometric oxidizer to fuel ratio (O/F) of a given mixture of oxidizer and fuel.
  Elements that can be included in the mixture are: C (carbon) H (Hydrogen) O(Oxygen) N(Nitrogen) Ar(Argon) He(Helium)
  Inputs: Species, Moles inert per moles oxidizer  (example: for a mixture of air and methane, species = {'O2', 'N2', 'CH4'} 
         MolesperMoleIOxidizer=3.76
  Outputs: OF_Stoich  (mass-based stoichiometric Oxidizer to fuel ratio) Molarray (moles of oxidizer, inert, and fuel at OF_Stoich, 
          assuming 1 mole of fuel)
Requires Subfunctions:
    1)CHON_MW.m
    2)ParseElementString.m

PhiToMoles -
 M Hageman 11/2019
 Determines mole fractions from fuel/oxidizer mixtures at multiple equivalence ratios
 Elements that can be included in the mixture are: C (carbon) H (Hydrogen) O(Oxygen) N(Nitrogen) Ar(Argon) He(Helium)
 Inputs: Species (ex: {'CH4' 'O2' 'N2'}, PhiRange (ex: [0.7 0.1 1.5] = [low step high]), MolesInertperMoleOxidizer (ex: 3.76 for air)
 Outputs: MoleFractionArray (mole fractions at each equivalence ratio)
 Uses Functions
    1)CHON_MW.m
    2)ParseElementString.m
    3)FindStoich.m
