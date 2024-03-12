import os
import matplotlib.pyplot as plt
from Bio import SeqIO
import numpy as np
from scipy.spatial.distance import pdist, squareform, euclidean
from sklearn.manifold import MDS

def process_sequences(variant_name):

    variant_dir = os.path.join("SARS_CoV_2_Variants", variant_name)
    os.makedirs(variant_dir, exist_ok=True)

    cgr_plot_dir = os.path.join("CGR_plots_delta", variant_name)
    os.makedirs(cgr_plot_dir, exist_ok=True)

    with open(f"{variant_name}.fasta", "r") as file:
        sequences = list(SeqIO.parse(file, "fasta"))

    cgr_matrices = []

    for i, record in enumerate(sequences, start=1):
        sequence = str(record.seq).upper()

        sequence = ''.join(letter for letter in sequence if letter in 'ACGT')

        with open(os.path.join(variant_dir, f"{variant_name}_{i}.fasta"), "w") as output_file:
            output_file.write(f">{record.description}\n{sequence}\n")

        k_value = 7
        cgr_matrix = cgr(seq=sequence, order="ACGT", k=k_value)
        cgr_matrices.append(np.array(cgr_matrix))  

        plt.imshow(cgr_matrix, cmap='viridis', interpolation='nearest')
        plt.title(f'CGR Plot for {variant_name}_{i}')
        plt.savefig(os.path.join(cgr_plot_dir, f'CGR_Plot_{variant_name}_{i}.png'))
        plt.close() 

    flattened_cgr_matrices = [cgr_matrix.flatten() for cgr_matrix in cgr_matrices]
    pairwise_distances = pdist(flattened_cgr_matrices, metric=euclidean)

    pairwise_distances_matrix = squareform(pairwise_distances)

    mds = MDS(n_components=3, dissimilarity='precomputed')
    embedded_coordinates = mds.fit_transform(pairwise_distances_matrix)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(embedded_coordinates[:, 0], embedded_coordinates[:, 1], embedded_coordinates[:, 2])
    ax.set_title(f'MDS Visualization for {variant_name}')
    plt.show()

def cgr(seq, order, k):
    ln = len(seq)
    pw = 2**k
    out = np.zeros((pw, pw))  
    x = 2**(k-1)
    y = 2**(k-1)

    for i in range(0, ln):
        x = x // 2
        y = y // 2
        if seq[i] == order[2] or seq[i] == order[3]:
            x = x + (2**(k-1))
        if seq[i] == order[0] or seq[i] == order[3]:
            y = y + (2**(k-1))
        if i >= k-1:
            out[y][x] = out[y][x] + 1

    return out

process_sequences("Delta")
