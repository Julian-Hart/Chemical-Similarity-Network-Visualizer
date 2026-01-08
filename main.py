import pubchempy as pcp

def create_compound_dictionary(compoundList):
    compoundDict = {}
    for compound in compoundList:
        try:
            compoundDataList = pcp.get_compounds(compound, "name")
            compoundDict[compound] = compoundDataList[0].smiles
        except:
            print(f"compound {compound} not found")
    return compoundDict


if __name__ == "__main__":
    compoundList = ["Aspirin", "Tylenol"]
    print(create_compound_dictionary(compoundList))

