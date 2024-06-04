from CHON_MW import CHON_MW
from ParseElementString import ParseElementString

def FindStoich(Species, MolesInertperMoleOxidizer):
    # Function to calculate stoichiometric ratios for combustion
    # Written in Matlab by M Hageman 11/2018
    #Converted to Python 9/18/2023 using ChatGPT

    # Inputs:
    # Species = ['CH4', 'O2', 'N2']
    # MolesInertperMoleOxidizer - as in Air = O2 + 3.76 N2

    # Outputs:
    # OF_Stoich - mass-based stoichiometric Oxidizer to fuel ratio
    # Inert - considered part of oxidizer - as in Air = O2 + 3.76 N2

    Fuel = Species[0]
    Oxidizer = Species[1]
    if len(Species) == 3:
        Inert = Species[2]
    else:
        Inert = '0'

    # Parse Fuel String
    FuelEleList, FuelNumList = ParseElementString(Fuel)
    FindC = [ele == 'C' for ele in FuelEleList]
    FindH = [ele == 'H' for ele in FuelEleList]
    FindO = [ele == 'O' for ele in FuelEleList]
    FindN = [ele == 'N' for ele in FuelEleList]
    FuelCarbon = sum([FindC[i] * FuelNumList[i] for i in range(len(FuelEleList))])
    FuelHydrogen = sum([FindH[i] * FuelNumList[i] for i in range(len(FuelEleList))])
    FuelOxygen = sum([FindO[i] * FuelNumList[i] for i in range(len(FuelEleList))])
    FuelNitrogen = sum([FindN[i] * FuelNumList[i] for i in range(len(FuelEleList))])
    FuelMW = CHON_MW(Fuel)

    # Parse Oxidizer String
    OxEleList, OxNumList = ParseElementString(Oxidizer)
    FindH = [ele == 'H' for ele in OxEleList]
    FindO = [ele == 'O' for ele in OxEleList]
    FindN = [ele == 'N' for ele in OxEleList]
    OxidizerHydrogen = sum([FindH[i] * OxNumList[i] for i in range(len(OxEleList))])
    OxidizerOxygen = sum([FindO[i] * OxNumList[i] for i in range(len(OxEleList))])
    OxidizerNitrogen = sum([FindN[i] * OxNumList[i] for i in range(len(OxEleList))])
    OxidizerMW = CHON_MW(Oxidizer)

    # Inert String is irrelevant. Only need MW.
    InertMW = CHON_MW(Inert)

    # Stoichiometric Equations
    x = FuelCarbon
    y = FuelHydrogen
    z = FuelOxygen
    w = OxidizerNitrogen
    v = OxidizerOxygen

    n1 = x
    n2 = y / 2
    a = ((2 * n1) + n2 - z) / v

    MolesFuel = 1
    MolesOxidizer = a
    MolesInert = a * MolesInertperMoleOxidizer
    Molarray = [MolesFuel, MolesOxidizer, MolesInert]

    OF_Stoich = (a * (OxidizerMW + MolesInertperMoleOxidizer * InertMW)) / FuelMW
    return OF_Stoich, Molarray
