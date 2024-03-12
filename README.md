# Data-Science-Project-Genomic-Analysis-of-SARS-Covid-Delta-Variant.

## Overview
Built a genomic analysis tool utilizing python programming languages to download, clean, and process SARS-CoV-Delta sequences of Prince edward island,Canada from the GISAID website. Successfully executed Chaos Game Representation (CGR) and multi-dimensional scaling (MDS) techniques, resulting in 3D visualizations that provided quantifiable insights into genomic relationships among variants. This project was recognized for its innovation, achieved success in streamlining data handling and computational analysis for biological datasets.

## Table of Contents

- [Installation](#Installation)
- [Usage](#Usage)
- [Project Discription](#Project_Discription)
- [Achievements](#Achievements)
- [Screenshots](#Screenshots)

## Installation
Clone the repository to your local machine.
Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Execute Script_1 to download, clean, and set up the dataset.
Execute Script_2 to read the dataset, compute Chaos Game Representations, calculate distances, and visualize relationships in 3D.
```bash
python script_1.py
python script_2.py
```

## Project Description
The Genomic Analysis Tool for SARS-CoV-2 Variants is a comprehensive project aimed at mastering key aspects of data science, including data downloading and cleaning, dataset setup, distance computation, dimensionality reduction, and data visualization. This project, involves two program scripts.

#### Program Script#1: Downloading and Pre-processing Data
Step 1 : Register on the GISAID site, following the instructions in the "Registration" tab. Account approval may take 24-48 hours.

Step 2 : Log in, navigate to the "EpiCoV" tab, and download SARS-CoV-2 sequences in "fasta" format. Apply filters for completeness, coverage, geographic origin, and variant type.

Step 3 : Process downloaded sequences for each variant, converting to uppercase, filtering recognized letters (A, C, G, T), and organizing them into individual .fasta files.

#### Program Script#2: Reading the Dataset and Visualization
Step 4 : Read individual .fasta files containing SARS-CoV-2 sequences.

Step 5 : Compute Chaos Game Representations (CGR) with k = 7 for each sequence, generating CGR plots.

Step 6 : Compute pairwise distances between CGRs, creating a symmetric distance matrix.

Step 7 : Utilize multi-dimensional scaling (MDS) for dimensionality reduction, creating a 3D plot to visualize relationships between data points.

## Achievements
This assignment was successfully completed using Python, incorporating libraries such as Biopython for sequence processing, Matplotlib for plotting, and Scikit-learn for MDS. The code includes optimized functions for reading sequences, generating CGR plots, computing distances, and visualizing relationships.

## Screenshots
![3D Plot Screenshot.png](3D%20Plot%20Screenshot.png)



