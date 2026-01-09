import pubchempy as pcp
from rdkit.Chem  import AllChem, MolFromSmiles


def create_compound_dictionary(compoundList):
    compoundDict = {}
    for compound in compoundList:
        try:
            compoundDataList = pcp.get_compounds(compound, "name")
            compoundDict[compound] = compoundDataList[0].smiles
        except:
            print(f"compound {compound} not found")
    return compoundDict


def create_fingerprints(compoundDict):
    compoundFingerprintDict = {}
    for compound in compoundDict.keys():
        fpgen = AllChem.GetRDKitFPGenerator()
        print(compoundDict[compound])
        compoundFingerprintDict[compound] = fpgen.GetFingerprint(MolFromSmiles(compoundDict[compound]))

    return compoundFingerprintDict
    

if __name__ == "__main__":
    compoundList = ["Aspirin", "Tylenol"]
    compoundDict = create_compound_dictionary(compoundList)
    print(create_fingerprints(compoundDict))

