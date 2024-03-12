import os
from Bio import SeqIO


def process_sequences(variant_name):
    variant_dir = os.path.join("SARS_CoV_2_Variants", variant_name)
    os.makedirs(variant_dir, exist_ok=True)

    with open(f"{variant_name}.fasta", "r") as file:
        sequences = list(SeqIO.parse(file, "fasta"))

    for i, record in enumerate(sequences, start=1):
        sequence = str(record.seq).upper()

        sequence = ''.join(letter for letter in sequence if letter in 'ACGT')

        with open(os.path.join(variant_dir, f"{variant_name}_{i}.fasta"), "w") as output_file:
            output_file.write(f">{record.description}\n{sequence}\n")


process_sequences("Delta")