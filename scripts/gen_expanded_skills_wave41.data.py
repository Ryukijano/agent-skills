SKILLS = [
    {
        "name": "ai-for-epigenomics",
        "title": "AI for Epigenomics",
        "description": "DNA methylation, histone modifications, chromatin accessibility, enhancer-promoter interactions, and deep learning models of gene regulation.",
        "devin_body": r'''## When to use

You are working with DNA methylation, histone modifications, chromatin accessibility, or other epigenomic assays and want to predict regulatory states, annotate genomic elements, or integrate epigenomic data with expression or phenotype data.

## Key concepts

- **DNA methylation**: CpG and non-CpG methylation patterns, often measured by WGBS or array-based assays.
- **Histone modifications**: ChIP-seq marks such as H3K4me3, H3K27ac, and H3K27me3 that define promoters and enhancers.
- **Chromatin accessibility**: ATAC-seq and DNase-seq that identify open regulatory regions.
- **Enhancer-promoter interactions**: 3D contact data linking distal regulatory elements to target genes.
- **Deep epigenomics models**: DeepSEA, Basenji, and Enformer-style sequence-to-activity predictors.

## Code pattern

```python
import numpy as np
import pyBigWig
from scipy.signal import find_peaks

# Load a bigWig track and scan a region for peaks
bw = pyBigWig.open("H3K27ac.bigWig")
values = np.array([v if v is not None else 0.0 for v in bw.values("chr1", 0, 1000000)])
peaks, _ = find_peaks(values, height=5.0, distance=1000)
```

## Tuning notes

- Use the same reference genome and blacklist regions for all samples.
- Normalize signal for sequencing depth and input control.
- Pay attention to class imbalance when training classifiers on peaks.
- Interpret models with attribution methods (e.g., Integrated Gradients) and motif analysis.

## Verification

1. Call peaks with a standard tool (MACS2/3) and compare overlap with model predictions.
2. Predict known enhancer activity and validate against matched RNA-seq or reporter data.
3. Evaluate the model on held-out chromosomes to estimate generalization.
''',
        "references": [
            "https://doi.org/10.1038/nrg3920",
            "https://doi.org/10.1038/s41576-025-00841-2",
            "https://doi.org/10.1016/j.compbiomed.2024.109302",
            "https://doi.org/10.1016/j.bbcan.2021.188588",
            "https://doi.org/10.3390/biomedicines9111733",
        ],
    },
    {
        "name": "ai-for-transcriptomics",
        "title": "AI for Transcriptomics",
        "description": "Bulk and single-cell RNA-seq analysis, normalization, clustering, differential expression, splicing, and foundation models for gene expression.",
        "devin_body": r'''## When to use

You need to quantify, normalize, cluster, or model gene expression from bulk RNA-seq or single-cell RNA-seq data for cell typing, differential expression, or gene regulation studies.

## Key concepts

- **Bulk vs single-cell RNA-seq**: population average versus cell-resolution expression.
- **Count normalization**: library size correction, log1p, and variance stabilization.
- **Dimensionality reduction**: PCA, UMAP, and latent embeddings for visualization and analysis.
- **Differential expression**: edgeR, DESeq2, or model-based tests across conditions or cell types.
- **Foundation models**: scBERT, scGPT, and scFoundation for cell representation and transfer learning.

## Code pattern

```python
import scanpy as sc

adata = sc.read_h5ad("scRNA.h5ad")
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=2000)
sc.tl.pca(adata)
```

## Tuning notes

- Filter low-quality cells and doublets before clustering.
- Choose a batch correction strategy (Harmony, scVI, Scanorama) when integrating datasets.
- Avoid overclustering by testing multiple resolution parameters.
- Use pseudotime and RNA velocity to interpret differentiation trajectories.

## Verification

1. Cluster the data and confirm known marker-gene expression.
2. Reproduce differential expression results with a second method (e.g., DESeq2 or MAST).
3. Project query cells onto a reference atlas and check annotation consistency.
''',
        "references": [
            "https://doi.org/10.1038/s41592-024-02353-z",
            "https://doi.org/10.1016/j.gpb.2022.11.011",
            "https://doi.org/10.1261/rna.080889.125",
            "https://doi.org/10.1038/s41592-019-0537-1",
            "https://doi.org/10.1038/s41592-024-02331-5",
        ],
    },
    {
        "name": "ai-for-metabolomics",
        "title": "AI for Metabolomics",
        "description": "Mass spectrometry and NMR metabolite profiling, annotation, pathway analysis, normalization, and machine learning for biomarker discovery.",
        "devin_body": r'''## When to use

You are analyzing mass spectrometry or NMR metabolomics data to identify metabolites, find biomarkers, classify samples, or integrate metabolism with other omics layers.

## Key concepts

- **LC-MS and NMR**: major analytical platforms for untargeted and targeted metabolomics.
- **Metabolite annotation**: matching m/z, retention time, and fragmentation to libraries.
- **Pathway analysis**: mapping features to KEGG, HMDB, and Reactome pathways.
- **Normalization**: batch, drift, and sample-wise scaling to remove technical variation.
- **Predictive models**: random forests, SVMs, and deep learning for biomarker discovery.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

df = pd.read_csv("metabolites.tsv", sep="\t")
X = df[metabolite_columns]
y = df["condition"]
model = RandomForestClassifier(n_estimators=500, random_state=42)
scores = cross_val_score(model, X, y, cv=5)
```

## Tuning notes

- Impute missing values carefully (k-NN, half-minimum, or probabilistic).
- Correct for batch effects with QC samples and ComBat or median batch alignment.
- Use internal validation (nested CV) to avoid overfitting high-dimensional data.
- Validate putative biomarkers with targeted assays.

## Verification

1. Reproduce principal-component separation by batch and condition.
2. Check whether significant features remain stable across independent cohorts.
3. Run pathway enrichment and confirm expected biology for the phenotype.
''',
        "references": [
            "https://doi.org/10.1016/j.trac.2024.117852",
            "https://doi.org/10.3390/metabo10060243",
            "https://doi.org/10.1002/smtd.202400305",
            "https://doi.org/10.3390/ijms231911269",
        ],
    },
    {
        "name": "ai-for-lipidomics",
        "title": "AI for Lipidomics",
        "description": "LC-MS/MS lipid species quantification, structural isomer resolution, lipid class normalization, and predictive modeling of lipid phenotypes.",
        "devin_body": r'''## When to use

You are quantifying or classifying lipid species from LC-MS/MS or shotgun lipidomics data and need to annotate lipid classes, correct for technical variation, or link lipid profiles to phenotypes.

## Key concepts

- **Lipid classes**: fatty acyls, glycerolipids, glycerophospholipids, sphingolipids, and sterols.
- **LC-MS/MS lipidomics**: separation and fragmentation for species and isomer resolution.
- **Epilipidomics**: post-translationally modified lipids and oxidation products.
- **LipidMaps**: curated lipid nomenclature and classification database.
- **Statistical modeling**: univariate tests, multivariate PCA, and supervised classifiers.

## Code pattern

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv("lipidomics.csv")
X = df[lipid_columns]
X_scaled = StandardScaler().fit_transform(X)
pcs = PCA(n_components=2).fit_transform(X_scaled)
```

## Tuning notes

- Normalize by total lipid class sum or internal standards.
- Handle structural isomers and annotation confidence levels.
- Correct for instrument batch and column drift.
- Be cautious of correlated lipid species in multivariate models.

## Verification

1. Inspect lipid class distributions for biological plausibility.
2. Replicate sample correlation and coefficient of variation across replicates.
3. Compare class separation in PCA to a priori group labels.
''',
        "references": [
            "https://doi.org/10.1007/s00216-023-04991-2",
            "https://doi.org/10.3390/biom11030473",
            "https://doi.org/10.1016/j.bbalip.2017.05.006",
            "https://doi.org/10.1021/acs.analchem.2c04406",
        ],
    },
    {
        "name": "ai-for-proteomics",
        "title": "AI for Proteomics",
        "description": "Mass spectrometry protein identification and quantification, DDA/DIA workflows, post-translational modifications, and AI-driven peptide property prediction.",
        "devin_body": r'''## When to use

You are analyzing mass spectrometry proteomics data to quantify proteins, identify post-translational modifications, build spectral libraries, or predict peptide properties.

## Key concepts

- **LC-MS/MS workflows**: DDA, DIA, SRM/PRM, and data-independent acquisition.
- **Peptide-spectrum matching**: search engines, spectral libraries, and rescoring.
- **Protein inference and FDR**: PSM, peptide, and protein-level false discovery rates.
- **PTMs**: phosphorylation, ubiquitination, glycosylation, and other modifications.
- **AI for proteomics**: retention time, fragmentation, and MHC-peptide binding prediction.

## Code pattern

```python
from pyteomics import mzml

# Iterate DDA spectra and parse precursor charge states
with mzml.read("run.mzML") as reader:
    for spectrum in reader:
        if spectrum["ms level"] == 2:
            prec = spectrum["precursorList"]["precursor"][0]
            ion = prec["selectedIonList"]["selectedIon"][0]
            print(ion["charge state"], ion["selected ion m/z"])
```

## Tuning notes

- Control FDR at PSM, peptide, and protein levels (1% typical).
- Normalize for total ion current or a reference channel.
- Impute missing values only after confirming MCAR/MAR mechanism.
- Choose DIA software (DIA-NN, Spectronaut, OpenSWATH) matched to library design.

## Verification

1. Benchmark identification and quantification on a public standard (e.g., iPRG, PXD).
2. Compare peptide-level fold changes to orthogonal western blot or PRM data.
3. Check retention time and ion intensity predictions against observed values.
''',
        "references": [
            "https://doi.org/10.1002/pmic.201900335",
            "https://doi.org/10.1038/s41587-022-01424-w",
            "https://doi.org/10.1016/j.crmeth.2021.100003",
            "https://doi.org/10.1002/pmic.202400398",
        ],
    },
    {
        "name": "ai-for-metagenomics",
        "title": "AI for Metagenomics",
        "description": "16S rRNA and shotgun microbial community profiling, taxonomic and functional prediction, MAG binning, and microbiome-host association modeling.",
        "devin_body": r'''## When to use

You are profiling microbial communities from 16S rRNA or shotgun metagenomic data to classify taxa, infer function, assemble MAGs, or link the microbiome to host phenotypes.

## Key concepts

- **Amplicon vs shotgun**: 16S rRNA profiling versus whole-genome metagenomics.
- **Taxonomic and functional profiling**: read classification, gene catalogues, and pathway inference.
- **Metagenome-assembled genomes (MAGs)**: binning contigs into draft microbial genomes.
- **Compositional data**: relative abundance, sparsity, and library size effects.
- **Host-microbiome models**: classification, time-series, and causal inference.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold

X = pd.read_csv("feature_table.tsv", sep="\t", index_col=0).T
y = pd.read_csv("metadata.tsv", sep="\t", index_col=0)["status"]
model = RandomForestClassifier(n_estimators=1000, random_state=42)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```

## Tuning notes

- Rarefy or use compositional transformations (CLR, ILR) with care.
- Remove contaminants and batch effects by including negative controls.
- Combine taxonomic and functional features for phenotype prediction.
- Validate on independent cohorts because microbiome associations rarely generalize.

## Verification

1. Reproduce alpha and beta diversity ordination.
2. Compare Random Forest, LASSO, and a compositional model on the same data.
3. Validate biomarkers in a geographically independent cohort.
''',
        "references": [
            "https://doi.org/10.1128/msystems.01642-24",
            "https://doi.org/10.1099/mgen.0.001231",
            "https://doi.org/10.3389/fmicb.2024.1516667",
            "https://doi.org/10.3389/fmicb.2023.1261889",
            "https://doi.org/10.3390/ijms26189206",
        ],
    },
    {
        "name": "ai-for-single-cell",
        "title": "AI for Single-Cell Omics",
        "description": "Single-cell transcriptomics, epigenomics, proteomics, and multi-omics integration, cell type annotation, trajectory inference, and foundation models.",
        "devin_body": r'''## When to use

You are working with single-cell genomics data (scRNA-seq, scATAC-seq, CITE-seq, or multi-omics) to annotate cell types, infer trajectories, integrate batches, or predict perturbation responses.

## Key concepts

- **scRNA-seq**: gene expression at single-cell resolution with dropout and high dimensionality.
- **scATAC and multi-omics**: chromatin accessibility and surface proteins in the same cells.
- **Batch correction and integration**: mapping new datasets to reference atlases.
- **Trajectory inference**: pseudotime, RNA velocity, and differentiation dynamics.
- **Foundation models**: scGPT, scBERT, and UCE for transfer learning and prediction.

## Code pattern

```python
import scanpy as sc

adata = sc.read_h5ad("scMultiome.h5ad")
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=3000)
sc.tl.pca(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)
```

## Tuning notes

- Remove ambient RNA and doublets before clustering.
- Choose integration method based on whether you need batch correction or atlas projection.
- Resolve subpopulations by testing marker genes and multiple resolutions.
- Use perturbation and time-series models to interpret dynamics.

## Verification

1. Assign cell types and compare to a reference atlas or known markers.
2. Project held-out batches and evaluate mixing vs biological conservation.
3. Validate trajectory ordering with time-course or lineage-tracing data.
''',
        "references": [
            "https://doi.org/10.1016/j.coisb.2021.04.006",
            "https://doi.org/10.1093/bioinformatics/btae374",
            "https://doi.org/10.1038/s41592-024-02353-z",
            "https://doi.org/10.1038/s41592-025-02856-3",
        ],
    },
    {
        "name": "ai-for-spatial-omics",
        "title": "AI for Spatial Omics",
        "description": "Spatially resolved transcriptomics and proteomics, cell segmentation, neighborhood analysis, and integration with imaging data.",
        "devin_body": r'''## When to use

You are analyzing spatially resolved transcriptomics, proteomics, or multi-omics data and need to account for tissue context, neighborhood structure, and image features.

## Key concepts

- **Spatial transcriptomics**: Visium, Slide-seq, Xenium, MERFISH, Stereo-seq, and seqFISH.
- **Spatial proteomics**: imaging mass cytometry, CODEX, and MIBI-TOF.
- **Cell segmentation and deconvolution**: mapping spots or pixels to cell types.
- **Neighborhood and interaction**: spatial domains, cell-cell communication, and niches.
- **Spatially variable genes (SVGs)**: genes with expression patterns tied to location.

## Code pattern

```python
import scanpy as sc
import squidpy as sq

adata = sc.read_h5ad("visium.h5ad")
sq.gr.spatial_neighbors(adata, radius=1.5)
sq.gr.spatial_autocorr(adata, mode="moran", genes=adata.var_names[:100])
sq.gr.nhood_enrichment(adata, cluster_key="cell_type")
```

## Tuning notes

- Align H&E images and spatial coordinates carefully.
- Choose spot vs cell resolution based on the biological question.
- Use spatial-aware imputation when genes are lowly expressed.
- Compare to matched single-cell data for deconvolution quality.

## Verification

1. Identify spatially variable genes and compare to known tissue markers.
2. Validate cell-type deconvolution against matched scRNA-seq or IHC.
3. Inspect neighborhood enrichment results for biologically expected ligand-receptor pairs.
''',
        "references": [
            "https://doi.org/10.1186/s13059-022-02653-7",
            "https://doi.org/10.1063/5.0091135",
            "https://doi.org/10.1093/bib/bbae719",
            "https://squidpy.readthedocs.io/en/stable/",
        ],
    },
    {
        "name": "ai-for-functional-genomics",
        "title": "AI for Functional Genomics",
        "description": "Predicting gene regulatory function from sequence and epigenomic data, mapping cis-regulatory elements, and interpreting non-coding variants.",
        "devin_body": r'''## When to use

You want to predict gene regulatory function from DNA sequence, map cis-regulatory elements, interpret genetic variants, or link epigenomic and transcriptomic states.

## Key concepts

- **Regulatory grammar**: how TF motifs, chromatin, and sequence context encode activity.
- **Functional assays**: ChIP-seq, ATAC-seq, MPRA, STARR-seq, and CAGE.
- **Sequence-to-function models**: DeepSEA, Basset, Enformer, and Basenji.
- **Variant effect prediction**: scoring non-coding variants for regulatory impact.
- **TF binding and expression**: linking enhancer states to target genes.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

# One-hot encode a DNA sequence (A=1000, C=0100, G=0010, T=0001)
def onehot(seq):
    mapping = {"A": 0, "C": 1, "G": 2, "T": 3}
    arr = np.zeros((len(seq), 4), dtype=int)
    for i, b in enumerate(seq):
        arr[i, mapping[b]] = 1
    return arr.flatten()

X = np.array([onehot(s) for s in sequences])
y = np.array(regulatory_activity)
model = GradientBoostingRegressor(n_estimators=500).fit(X, y)
```

## Tuning notes

- Match model input length to the assay (e.g., 1 kb for ChIP, 100 kb for Enformer).
- Use the same reference genome and avoid train/test leakage across chromosomes.
- Balance classes or use regression losses for continuous activity.
- Interpret with motif and variant scoring, not just overall accuracy.

## Verification

1. Compare predicted regulatory activity to matched ChIP/ATAC signal.
2. Score known GWAS fine-mapped variants and check enrichment in predicted enhancers.
3. Test generalization on a different cell type or held-out chromosome.
''',
        "references": [
            "https://doi.org/10.1146/annurev-biodatasci-020722-115651",
            "https://doi.org/10.1038/s41592-024-02331-5",
            "https://doi.org/10.1016/j.csbj.2021.07.021",
            "https://doi.org/10.1038/s41576-019-0122-6",
        ],
    },
    {
        "name": "ai-for-structural-genomics",
        "title": "AI for Structural Genomics",
        "description": "3D genome organization, Hi-C analysis, protein structure prediction with deep learning, and multiscale structural modeling.",
        "devin_body": r'''## When to use

You are studying the three-dimensional organization of genomes, protein structures, or chromatin conformations and need to predict, analyze, or model spatial molecular structures.

## Key concepts

- **3D genome organization**: chromatin loops, topologically associating domains (TADs), and A/B compartments.
- **Hi-C and related assays**: chromosome conformation capture at scale.
- **Protein structure prediction**: AlphaFold and related deep learning models.
- **Multiscale modeling**: integrating sequence, imaging, and polymer physics.
- **Structural variation**: linking genome folding to gene regulation and disease.

## Code pattern

```python
import cooler
import numpy as np
import cooltools

c = cooler.Cooler("hic.cool")
mat = c.matrix(balance=True).fetch("chr1:0-10000000")
insulation = cooltools.insulation(c, 100000)
```

## Tuning notes

- Choose resolution (1 kb to 100 kb) based on feature size.
- Apply bias correction (ICE/VC) before downstream analysis.
- Distinguish static structural maps from dynamic conformational ensembles.
- Integrate imaging data (FISH, super-resolution) to validate 3D models.

## Verification

1. Call TADs and loops with multiple tools (cooltools, Arrowhead) and compare overlap.
2. Compare A/B compartments from Hi-C PCA to known epigenomic marks.
3. Validate a predicted 3D structure against FISH or microscopy distances.
''',
        "references": [
            "https://doi.org/10.1038/s41576-023-00638-1",
            "https://doi.org/10.1038/s44320-024-00016-x",
            "https://doi.org/10.1038/s41576-019-0122-6",
            "https://doi.org/10.1007/s00018-025-05837-z",
        ],
    },
    {
        "name": "ai-for-comparative-genomics",
        "title": "AI for Comparative Genomics",
        "description": "Cross-species and population genome comparison, orthology inference, phylogenomics, selection scans, and pan-genome analysis.",
        "devin_body": r'''## When to use

You are comparing genomes across species, strains, or populations to infer evolution, identify conserved regions, build phylogenies, or study pan-genomes.

## Key concepts

- **Homology and orthology**: orthologous genes, paralogs, and orthogroups.
- **Genome alignment and synteny**: whole-genome and multiple alignments.
- **Phylogenetics and phylogenomics**: tree inference, gene trees, and species trees.
- **Population genomics**: selection, demographic history, and introgression.
- **Pan-genomes**: core, shell, and accessory gene content.

## Code pattern

```python
from Bio import AlignIO

alignment = AlignIO.read("genomes.aln", "fasta")
length = alignment.get_alignment_length()
variable = []
for i in range(length):
    column = [rec.seq[i] for rec in alignment]
    if len(set(column)) > 1:
        variable.append(i)
print("Variable sites:", len(variable))
```

## Tuning notes

- Use high-quality, chromosome-scale assemblies for whole-genome alignment.
- Account for incomplete lineage sorting and horizontal gene transfer.
- Choose substitution and indel models matched to data (codon, nucleotide, amino acid).
- Validate orthology with synteny and reciprocal best hits.

## Verification

1. Compare a phylogenetic tree to a published species tree or fossil record.
2. Test for selection with dN/dS or population genetics scans.
3. Map structural variants and check conservation in outgroup genomes.
''',
        "references": [
            "https://doi.org/10.1016/j.ympev.2024.108066",
            "https://doi.org/10.1038/s41576-023-00636-3",
            "https://doi.org/10.1186/s13059-022-02735-6",
            "https://doi.org/10.3390/app14114837",
        ],
    },
    {
        "name": "ai-for-immunogenomics",
        "title": "AI for Immunogenomics",
        "description": "MHC and peptide binding prediction, TCR/BCR repertoire analysis, epitope and neoantigen prediction, and immunoinformatics.",
        "devin_body": r'''## When to use

You are studying immune receptor repertoires, MHC-peptide binding, T/B cell responses, neoantigens, or vaccine design and want to predict or analyze immunogenic sequences.

## Key concepts

- **MHC/HLA**: human leukocyte antigen molecules and peptide binding grooves.
- **TCR and BCR repertoires**: V(D)J recombination and clonotype analysis.
- **Epitope prediction**: MHC class I/II binding, antigen processing, and presentation.
- **Neoantigens**: tumor-specific mutations that can elicit T-cell responses.
- **Immunopeptidomics**: mass spectrometry of MHC-presented peptides.

## Code pattern

```python
from mhcflurry import Class1PresentationPredictor

predictor = Class1PresentationPredictor.load()
predictions = predictor.predict(
    peptides=["SIINFEKL", "NLVPMVATV"],
    alleles=["HLA-A*02:01"]
)
print(predictions[["peptide", "mhcflurry_presentation_percentile"]])
```

## Tuning notes

- Choose prediction tools (NetMHCpan, MHCflurry, MixMHCpred) matched to available data.
- Distinguish MHC binding from antigen processing and immunogenicity.
- Account for HLA allele diversity and population coverage.
- Validate in vitro before clinical or vaccine decisions.

## Verification

1. Benchmark MHC predictions against a measured binding or elution dataset.
2. Compare predicted epitopes to NetMHCpan and validate with a subset by experiment.
3. Calculate HLA coverage and neoantigen load for a given population.
''',
        "references": [
            "https://doi.org/10.1038/s41541-025-01258-y",
            "https://doi.org/10.1146/annurev-biodatasci-021920-100259",
            "https://doi.org/10.1146/annurev-immunol-082119-124838",
            "https://doi.org/10.1371/journal.pcbi.1006457",
            "https://doi.org/10.1093/bib/bbz051",
        ],
    },
]
