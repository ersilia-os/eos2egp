import os
import csv
import sys
import re
import numpy as np
from rdkit import Chem
from ersilia_pack_utils.core import read_smiles, write_out

input_file = sys.argv[1]
output_file = sys.argv[2]

root = os.path.dirname(os.path.abspath(__file__))
smarts_file = os.path.join(root, "Chelator_Rule.txt")


def _sanitize_name(name):
    name = name.lower()
    name = name.replace("*", "_star")
    name = re.sub(r"[\s,\-]+", "_", name)
    name = re.sub(r"_+", "_", name)
    return name.strip("_")


def _load_patterns(path):
    patterns = []
    with open(path, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for row in reader:
            col_name = _sanitize_name(row[0].strip())
            mol_patt = Chem.MolFromSmarts(row[1].strip())
            patterns.append((col_name, mol_patt))
    return patterns


patterns = _load_patterns(smarts_file)
headers = [name for name, _ in patterns] + ["n_hits"]
empty_output = [None] * len(patterns) + [None]


def my_model(smiles_list):
    results = []
    for smi in smiles_list:
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            results.append(empty_output)
            continue
        row = [
            1 if patt is not None and mol.HasSubstructMatch(patt) else 0
            for _, patt in patterns
        ]
        results.append(row + [sum(row)])
    return results


_, smiles_list = read_smiles(input_file)
outputs = my_model(smiles_list)

assert len(smiles_list) == len(outputs)

write_out(outputs, headers, output_file, np.float32)
