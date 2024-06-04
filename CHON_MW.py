def CHON_MW(SpeciesName):
    #Use parsed C,H,O,N,He,Ar molecule elements to find MW
    #Original Matlab Script: M. Hageman 11/2018
    #Converted to Python using ChatGPT 9/18/2023

    #Inputs:
    #SpeciesName example: 'CH4' or 'O2' etc.  Only CHON+Ar+He containing molecules will work.

    #Outputs:
    #MW - molecular weight of the input species [kg/kmol or g/mol]

    #Requires Subfunctions:
    #ParseElementString(str)


    # List of CHON elements and their corresponding molecular weights
    CHON = ['C', 'H', 'O', 'N', 'Ar', 'He']
    CHON_MW = [12.011, 1.008, 15.999, 14.007, 39.948, 4.003]

    MW_Element = []
    MW_Atoms = []

    # Assuming ParseElementString is a Python script in the same folder
    from ParseElementString import ParseElementString

    # Parse the input species name
    ElementList, NumberList = ParseElementString(SpeciesName)

    # Loop through the elements and calculate molecular weights
    for element, number in zip(ElementList, NumberList):
        if element in CHON:
            loc = CHON.index(element)  # Find the index of the element in CHON list
            MW_Element.append(CHON_MW[loc])  # Append the molecular weight of the element
            MW_Atoms.append(CHON_MW[loc] * number)  # Calculate the molecular weight for this element

    MW = sum(MW_Atoms)  # Sum the molecular weights of all elements to get the total
    return MW