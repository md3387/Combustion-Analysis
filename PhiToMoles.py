from FindStoich import FindStoich

def PhiToMoles(Species, MolesInertperMoleOxidizer, PhiRange):
    # Mole fractions of multiple equivalence ratios

    # Inputs:
    # Species = ['CH4', 'O2', 'N2']
    # PhiRange = [0.7, 0.1, 1.5]  # [low, step, high]
    # MolesInertperMoleOxidizer = 3.76  # for air

    # Uses Functions: FindStoich, CHON_MW, ParseElementString

    OF_Stoich, MolArrayStoich = FindStoich(Species, MolesInertperMoleOxidizer)
    i = 0
    ReportPhi = []
    FuelMoles = []
    OxidizerMoles = []
    InertMoles = []
    MolarFraction = []

    for Phi in range(int(PhiRange[0] * 10), int((PhiRange[2] + 0.1) * 10), int(PhiRange[1] * 10)):
        i += 1
        ReportPhi.append(Phi / 10)
        FuelMoles.append(1)
        OxidizerMoles.append(MolArrayStoich[1] / (Phi / 10))
        InertMoles.append(OxidizerMoles[i - 1] * MolesInertperMoleOxidizer)
        MolarFraction.append(FuelMoles[i - 1] / (OxidizerMoles[i - 1] + InertMoles[i - 1]))

    MoleFractionArray = list(zip(ReportPhi, FuelMoles, OxidizerMoles, InertMoles, MolarFraction))
    return MoleFractionArray
