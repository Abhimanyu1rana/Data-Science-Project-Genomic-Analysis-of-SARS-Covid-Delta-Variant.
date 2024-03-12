# Data-Science-Project-Genomic-Analysis-of-SARS-Covid-Delta-Variant.
## Data Science Project: Genomic Analysis of SARS-Covid-Delta Variant.
Built a genomic analysis tool utilizing python programming languages to download, clean, and process SARS-CoV-Delta sequences of Prince edward island,Canada from the GISAID website. Successfully executed Chaos Game Representation (CGR) and multi-dimensional scaling (MDS) techniques, resulting in 3D visualizations that provided quantifiable insights into genomic relationships among variants. This project was recognized for its innovation, achieved success in streamlining data handling and computational analysis for biological datasets.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/yourusername/genomic-analysis-tool.git
Install dependencies:
bash
Copy code
pip install -r requirements.txt

## Usage
Execute Script#1 to download, clean, and set up the dataset.
Execute Script#2 to read the dataset, compute Chaos Game Representations, calculate distances, and visualize relationships in 3D.
bash
Copy code
python script_1.py
python script_2.py
Project Description
The Genomic Analysis Tool for SARS-CoV-2 Variants is a comprehensive project aimed at mastering key aspects of data science, including data downloading and cleaning, dataset setup, distance computation, dimensionality reduction, and data visualization. This assignment, executed as part of a course, involves two program scripts.

Program Script#1: Downloading and Pre-processing Data
Step 1 (2 marks): Register on the GISAID site, following the instructions in the "Registration" tab. Account approval may take 24-48 hours.

Step 2 (2 marks): Log in, navigate to the "EpiCoV" tab, and download SARS-CoV-2 sequences in "fasta" format. Apply filters for completeness, coverage, geographic origin, and variant type.

Step 3 (3 marks): Process downloaded sequences for each variant, converting to uppercase, filtering recognized letters (A, C, G, T), and organizing them into individual .fasta files.

Program Script#2: Reading the Dataset and Visualization
Step 4 (2 marks): Read individual .fasta files containing SARS-CoV-2 sequences.

Step 5 (3 marks): Compute Chaos Game Representations (CGR) with k = 7 for each sequence, generating CGR plots.

Step 6 (4 marks): Compute pairwise distances between CGRs, creating a symmetric distance matrix.

Step 7 (4 marks): Utilize multi-dimensional scaling (MDS) for dimensionality reduction, creating a 3D plot to visualize relationships between data points.

Achievements and Code
This assignment was successfully completed using Python, incorporating libraries such as Biopython for sequence processing, Matplotlib for plotting, and Scikit-learn for MDS. The code includes optimized functions for reading sequences, generating CGR plots, computing distances, and visualizing relationships.
