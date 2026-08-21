SKILLS = [
    {
        "name": "ai-for-epigenomics",
        "title": "AI for Epigenomics",
        "description": "Use deep learning to predict gene-regulatory states and interpret non-coding variants from DNA methylation, histone marks, chromatin accessibility and 3D contact data.",
        "devin_body": r'''## When to use

You are working with DNA methylation, histone modifications, chromatin accessibility, or other epigenomic assays and want to predict regulatory states, annotate genomic elements, or integrate epigenomic data with expression or phenotype data.

## Usage

- **Predict DNA methylation**: identify regulatory and imprinting changes from WGBS or array data.
- **Classify enhancers and promoters**: use ChIP-seq marks such as H3K4me3, H3K27ac, and H3K27me3.
- **Model chromatin accessibility**: interpret ATAC-seq and DNase-seq to find open regulatory regions.
- **Link distal elements**: connect enhancers to target genes with 3D contact and HiChIP data.
- **Score variants**: predict the impact of non-coding variants and interpret with motif and attribution analysis.

## Steps

1. Collect and align WGBS, ChIP-seq, ATAC-seq, or array data to the same reference and blacklist.
2. Call peaks or quantify signals, normalize for depth and input control, and annotate genomic regions.
3. Train or load a sequence-to-activity model such as Enformer, Basenji, or Corgi on genomic windows.
4. Annotate enhancers, promoters, and 3D contacts and link distal elements to target genes.
5. Score variants and interpret predictions with motif analysis and attribution maps.
6. Validate predicted regulatory effects against reporter assays, RNA-seq, or matched epigenomic profiles.

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
        "description": "Use machine learning and foundation models to quantify, normalize and interpret bulk and single-cell RNA-seq data for cell typing, differential expression and gene regulation.",
        "devin_body": r'''## When to use

You need to quantify, normalize, cluster, or model gene expression from bulk RNA-seq or single-cell RNA-seq data for cell typing, differential expression, or gene regulation studies.

## Usage

- **Preprocess counts**: filter, normalize, and stabilize variance for bulk and single-cell RNA-seq.
- **Reduce dimensions**: run PCA, UMAP, or latent embeddings for visualization and analysis.
- **Detect differential expression**: identify genes across conditions or cell types with appropriate tests.
- **Apply foundation models**: use scBERT, scGPT, and scFoundation for representation and transfer learning.
- **Reconstruct trajectories**: infer pseudotime, RNA velocity, and lineage dynamics.

## Steps

1. Load raw counts and metadata, filter low-quality cells/genes, and normalize for library size.
2. Select highly variable genes and compute dimensionality reduction and embeddings.
3. Cluster cells or samples and annotate them with known marker genes or reference atlases.
4. Test for differential expression between conditions and validate with a second method.
5. Build or apply a foundation model for transfer learning, imputation, or perturbation prediction.
6. Compare results to reference atlases and orthogonal assays to assess biological consistency.

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
        "description": "Use machine learning on LC-MS, GC-MS and NMR metabolite profiles to annotate features, discover biomarkers and predict disease risk or metabolic phenotypes.",
        "devin_body": r'''## When to use

You are analyzing mass spectrometry or NMR metabolomics data to identify metabolites, find biomarkers, classify samples, or integrate metabolism with other omics layers.

## Usage

- **Process spectra**: convert LC-MS, GC-MS, and NMR data into aligned peak tables and features.
- **Annotate metabolites**: match m/z, retention time, and fragmentation to reference libraries.
- **Normalize data**: correct batch effects, drift, and sample size before modeling.
- **Map pathways**: connect significant features to KEGG, HMDB, and Reactome pathways.
- **Predict phenotypes**: train classifiers and risk scores for disease and patient stratification.

## Steps

1. Import raw spectral or peak-table data and apply quality control and missing-value imputation.
2. Annotate metabolites with m/z, RT, MS/MS libraries, or NMR chemical-shift databases.
3. Normalize and correct for batch effects using QC samples or statistical alignment.
4. Perform univariate, multivariate, or ML-based biomarker discovery with cross-validation.
5. Map significant features to metabolic pathways and interpret biological relevance.
6. Validate biomarkers with targeted assays and independent cohorts.

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
        "description": "Use machine learning on LC-MS/MS and shotgun lipidomics data to annotate lipid classes, resolve isomers, normalize variation and link lipid profiles to phenotypes.",
        "devin_body": r'''## When to use

You are quantifying or classifying lipid species from LC-MS/MS or shotgun lipidomics data and need to annotate lipid classes, correct for technical variation, or link lipid profiles to phenotypes.

## Usage

- **Classify lipids**: assign species to fatty acyls, glycerolipids, glycerophospholipids, sphingolipids, and sterols.
- **Resolve isomers**: use fragmentation and retention patterns to separate structural isomers and epilipidomics modifications.
- **Normalize signals**: scale by total lipid class sum or internal standards and correct batch drift.
- **Map nomenclature**: align annotations with LipidMaps and pathway databases.
- **Build phenotype models**: link lipid signatures to disease, diet, or intervention outcomes.

## Steps

1. Acquire LC-MS/MS or shotgun lipidomics data and apply peak picking and alignment.
2. Annotate lipid classes and molecular species with LipidMaps and MS/MS fragment rules.
3. Normalize intensities by class sums or internal standards and correct batch effects.
4. Perform PCA, univariate tests, or supervised classification on lipid features.
5. Validate isomer resolution and annotation confidence with reference standards.
6. Integrate lipid signatures with clinical or phenotypic data and replicate in independent cohorts.

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
        "description": "Use machine learning on mass-spectrometry proteomics data to improve peptide identification, quantify proteins, predict post-translational modifications and build spectral libraries for DDA and DIA workflows.",
        "devin_body": r'''## When to use

You are analyzing mass spectrometry proteomics data to quantify proteins, identify post-translational modifications, build spectral libraries, or predict peptide properties.

## Usage

- **Identify peptides**: process DDA and DIA LC-MS/MS data with search engines and spectral libraries.
- **Control FDR**: enforce 1% false discovery rates at PSM, peptide, and protein levels.
- **Predict peptide properties**: use deep learning for retention time, fragmentation, and ionization.
- **Detect PTMs**: identify and localize phosphorylation, glycosylation, ubiquitination, and other modifications.
- **Quantify proteins**: measure abundance changes across conditions and integrate with other omics.

## Steps

1. Convert raw MS files and build or choose a search database or spectral library.
2. Identify peptides with a search engine, control FDR, and infer proteins.
3. Train or apply deep learning models for retention time, fragmentation, or PTM prediction.
4. Quantify proteins across replicates and conditions with normalization and imputation.
5. Detect differentially abundant proteins and validate with orthogonal assays.
6. Share data and workflows in containers or repositories to support reproducibility.

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
        "description": "Use machine learning on 16S rRNA and shotgun metagenomic data to profile microbial communities, infer functions, assemble metagenome-assembled genomes and link the microbiome to host phenotypes.",
        "devin_body": r'''## When to use

You are profiling microbial communities from 16S rRNA or shotgun metagenomic data to classify taxa, infer function, assemble MAGs, or link the microbiome to host phenotypes.

## Usage

- **Profile taxonomy**: classify 16S amplicon or shotgun reads into taxonomic and functional profiles.
- **Assemble MAGs**: bin contigs into metagenome-assembled genomes and assess quality.
- **Handle composition**: apply CLR, ILR, or other transformations to relative-abundance data.
- **Model host associations**: link taxonomic and functional features to phenotype or intervention.
- **Validate generalization**: test microbiome associations in independent cohorts.

## Steps

1. Quality-filter and trim reads, remove contaminants, and account for negative controls.
2. Profile taxonomy from 16S or shotgun data, or assemble and bin MAGs from metagenomes.
3. Infer functional content with gene catalogs and pathway databases.
4. Apply compositional transformations and batch correction before statistical testing.
5. Train classification or regression models linking microbiome features to host phenotypes.
6. Validate associations in independent cohorts and confirm with targeted experiments.

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
        "description": "Use single-cell and multi-omics foundation models to annotate cell types, integrate batches, infer trajectories and predict perturbation responses.",
        "devin_body": r'''## When to use

You are working with single-cell genomics data (scRNA-seq, scATAC-seq, CITE-seq, or multi-omics) to annotate cell types, infer trajectories, integrate batches, or predict perturbation responses.

## Usage

- **Preprocess data**: normalize scRNA-seq, scATAC-seq, CITE-seq, or multi-omics profiles.
- **Remove artifacts**: filter ambient RNA, doublets, and low-quality cells before analysis.
- **Annotate cells**: identify types and novel subpopulations with marker genes and foundation models.
- **Integrate batches**: correct batch effects or map query data to reference atlases.
- **Model dynamics**: infer trajectories, RNA velocity, and perturbation responses with scGPT or scFoundation.

## Steps

1. Load single-cell data, filter low-quality cells and doublets, and normalize counts.
2. Select features and compute dimensionality reduction, neighbors, and embeddings.
3. Cluster cells and annotate them with marker genes or reference atlases.
4. Integrate multiple batches or project query data onto a reference while preserving biology.
5. Infer trajectories and velocity, or predict perturbation responses with foundation models.
6. Validate cell types and dynamics with orthogonal experiments or lineage-tracing data.

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
        "description": "Use machine learning on spatially resolved transcriptomics and proteomics to segment cells, analyze neighborhoods, integrate imaging and map tissue microenvironments.",
        "devin_body": r'''## When to use

You are analyzing spatially resolved transcriptomics, proteomics, or multi-omics data and need to account for tissue context, neighborhood structure, and image features.

## Usage

- **Process platforms**: analyze Visium, Slide-seq, Xenium, MERFISH, Stereo-seq, and seqFISH data.
- **Segment or deconvolve**: map spots or pixels to cell types using single-cell references.
- **Find spatial patterns**: identify spatially variable genes and tissue domains.
- **Model neighborhoods**: compute cell-cell communication, niches, and enrichment.
- **Integrate modalities**: combine with H&E images and matched single-cell data.

## Steps

1. Load spatial data and align coordinates with tissue images or H&E sections.
2. Preprocess expression, select spatially variable genes, and perform normalization.
3. Segment cells or deconvolve spots into cell-type proportions using single-cell references.
4. Build spatial neighbor graphs and compute spatial autocorrelation and domain detection.
5. Infer cell-cell communication, niches, and interactions in spatial neighborhoods.
6. Validate deconvolution and spatial patterns with IHC, smFISH, or matched scRNA-seq.

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
        "description": "Use sequence-to-function models to predict gene-regulatory activity, map cis-regulatory elements and interpret non-coding variants from genomic sequence and epigenomic data.",
        "devin_body": r'''## When to use

You want to predict gene regulatory function from DNA sequence, map cis-regulatory elements, interpret genetic variants, or link epigenomic and transcriptomic states.

## Usage

- **Map regulatory grammar**: infer TF motifs, chromatin, and sequence context.
- **Integrate assays**: combine ChIP-seq, ATAC-seq, MPRA, STARR-seq, and CAGE data.
- **Train sequence models**: build or apply DeepSEA, Basset, Enformer, Borzoi, or AlphaGenome.
- **Predict variant effects**: score non-coding and fine-mapped GWAS variants.
- **Interpret mechanisms**: link enhancers to genes and explain with motif and attribution analysis.

## Steps

1. Assemble reference genomes, blacklist regions, and collect functional assay data.
2. Preprocess and binarize or quantify regulatory activity across cell types and conditions.
3. Train or load a sequence-to-function model and evaluate on held-out chromosomes.
4. Score non-coding variants and fine-mapped GWAS loci for regulatory impact.
5. Interpret model predictions with motif discovery, attribution, and in silico mutagenesis.
6. Validate predicted regulatory effects with MPRA, reporter assays, or eQTL data.

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
        "description": "Use deep learning and polymer modeling to predict 3D genome organization, protein structures and chromatin conformations from sequence and contact data.",
        "devin_body": r'''## When to use

You are studying the three-dimensional organization of genomes, protein structures, or chromatin conformations and need to predict, analyze, or model spatial molecular structures.

## Usage

- **Predict genome folding**: model chromatin compartments, TADs, loops, and enhancer-promoter contacts.
- **Analyze contact data**: process Hi-C, Micro-C, and capture-C at multiple resolutions.
- **Predict protein structures**: run AlphaFold or related models for relevant genes.
- **Model structural variation**: assess the impact of variants on 3D organization and regulation.
- **Integrate scales**: combine sequence, imaging, and polymer physics for multiscale modeling.

## Steps

1. Align and normalize Hi-C or Micro-C data and choose resolution for the target feature size.
2. Call TADs, compartments, and loops with multiple tools and compare overlaps.
3. Train or apply a sequence-based 3D genome model such as Akita, Orca, or C.Origami.
4. Predict protein structures for relevant genes using AlphaFold or related models.
5. Score structural variants and design in silico perturbations of regulatory elements.
6. Validate 3D predictions with FISH, microscopy, or gene-expression changes.

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
        "description": "Use machine learning and phylogenomics to compare genomes across species and populations, infer orthology, detect selection and analyze pan-genomes.",
        "devin_body": r'''## When to use

You are comparing genomes across species, strains, or populations to infer evolution, identify conserved regions, build phylogenies, or study pan-genomes.

## Usage

- **Infer orthology**: identify orthologs and paralogs across species with graph or tree methods.
- **Build alignments**: create whole-genome, synteny, and protein alignments.
- **Reconstruct phylogeny**: infer species and gene trees and reconcile them.
- **Detect selection**: scan for positive selection, introgression, and demographic history.
- **Analyze pan-genomes**: build graphs of core, shell, and accessory gene content.

## Steps

1. Select high-quality assemblies and annotate genes with consistent pipelines.
2. Build whole-genome or protein alignments and infer orthogroups with graph or tree methods.
3. Reconstruct phylogenies and reconcile gene and species trees.
4. Scan for selection, introgression, and structural variants across lineages.
5. Build a pan-genome graph or variation graph and quantify core/shell/accessory content.
6. Validate orthology and selection signals with synteny, reciprocal best hits, and experiments.

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
        "description": "Use machine learning to predict MHC-peptide binding, analyze TCR and BCR repertoires, identify epitopes and neoantigens and support vaccine and immunotherapy design.",
        "devin_body": r'''## When to use

You are studying immune receptor repertoires, MHC-peptide binding, T/B cell responses, neoantigens, or vaccine design and want to predict or analyze immunogenic sequences.

## Usage

- **Predict MHC binding**: score MHC class I/II binding and antigen processing.
- **Analyze repertoires**: study V(D)J recombination and clonotype diversity in TCR and BCR data.
- **Find neoantigens**: identify tumor-specific peptides from somatic mutations and expression.
- **Integrate immunopeptidomics**: use mass spectrometry of HLA-bound peptides for antigen discovery.
- **Model TCR-pMHC pairing**: predict TCR recognition and HLA coverage for personalized vaccines.

## Steps

1. Collect HLA allele information and peptide or repertoire sequencing data.
2. Predict MHC binding, processing, and immunogenicity with NetMHCpan, MHCflurry, or similar.
3. Assemble TCR/BCR clonotypes and analyze repertoire diversity and expansion.
4. Call somatic mutations and expression to predict and prioritize neoantigens.
5. Validate predicted epitopes with binding, elution, or functional assays.
6. Compute population HLA coverage and design vaccine or cell-therapy candidates.

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