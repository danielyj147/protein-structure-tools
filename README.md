# 🧬 Protein Playground

A collection of Python scripts for exploring and analyzing protein 3D structures. This repository is a developer's sandbox for learning the basics of computational biology and bioinformatics using data from sources like the [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/).

## About This Project

This project was started as a "Hello, World" for a software developer with a background in Computer Science and Mathematics diving into the world of biology. The goal is to move beyond the high-level hype of tools like AlphaFold and get hands-on with the data they produce.

The scripts here use **Biopython** to parse `.pdb` files, perform calculations, and analyze the geometric properties of protein structures.

## Features

* **PDB Parser:** A simple script to parse `.pdb` files and print basic statistics (e.g., atom count, chain IDs, residues).
* **Center of Mass:** A script to calculate the geometric center (center of mass) of a protein structure.
* **Structure Comparison (RMSD):** A tool to superimpose two protein structures and calculate their Root Mean Square Deviation (RMSD) to see how similar they are.

## Getting Started

### Prerequisites

* [Python 3.12+](https://www.python.org/)
* [Biopython](https://biopython.org/)

### Installation

1. **Clone the repository:**

    ```bash
    git clone [https://github.com/danielyj147/protein-structure-tools.git](https://github.com/danielyj147/protein-structure-tools.git)
    cd protein-structure-tools
    ```

2. **Install dependencies:**
    (It's highly recommended to use UV)

    ```bash
    uv sync
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

## Usage

To run a script, simply pass it the path to a `.pdb` file.

**Example (using the info script):**

1. **Download a structure:**
    Go to the [AlphaFold DB](https://alphafold.ebi.ac.uk/) and search for a protein (e.g., E. coli, UniProt ID: `P76011`). Download the PDB file (e.g., `AF-P76011-F1-model_v6.pdb`).

2. **Run the script:**

    ```bash
    python parse_pdb.py AF-P76011-F1-model_v6.pdb
    ```

    **Expected Output:**

    ```text
    Structure ID: AF-P76011-F1-model_v6
    Total atoms: 619
    Residues: 84
    Chains: A
    ```

## Roadmap

* [ ] Add more complex geometric analysis (e.g., calculating distances between specific residues).
* [ ] Integrate a simple 3D viewer using a web library.
* [ ] Explore *de novo* protein sequences with ColabFold and analyze the results here.

## Citation

The protein structure data used in this project is sourced from the AlphaFold Protein Structure Database. If you use this data, please cite the original AlphaFold paper:

> Jumper, J., Evans, R., Pritzel, A. et al. Highly accurate protein structure prediction with AlphaFold. *Nature* **596**, 583–589 (2021). <https://doi.org/10.1038/s41586-021-03819-2>
