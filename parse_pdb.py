import sys
from Bio.PDB import PDBParser


def analyze_pdb(pdb_file_path):
    """
    Parses a PDB file and prints a summary of its contents.

    Args:
        pdb_file_path (str): The full path to the .pdb file.
    """
    try:
        structure_id = pdb_file_path.split("/")[-1].split(".")[0]

        parser = PDBParser(QUIET=True)  # QUIET=True suppresses warnings

        structure = parser.get_structure(structure_id, pdb_file_path)

        model = structure[0]

        atom_count = 0
        residue_count = 0
        chain_ids = []

        for chain in model:
            chain_ids.append(chain.id)
            for residue in chain:
                residue_count += 1
                for (
                    _
                ) in residue:
                    atom_count += 1

        print(f"Structure ID: {structure.id}")
        print(f"Total atoms: {atom_count}")
        print(f"Residues: {residue_count}")
        print(f"Chains: {', '.join(chain_ids)}")

    except FileNotFoundError:
        print(f"Error: The file '{pdb_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred while parsing the file: {e}")
        print("Please ensure it is a valid PDB file.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_pdb.py <path_to_pdb_file>")
        sys.exit(1) 

    pdb_file = sys.argv[1]

    analyze_pdb(pdb_file)
