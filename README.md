[![DOI](https://sandbox.zenodo.org/badge/395661559.svg)](https://sandbox.zenodo.org/doi/10.5072/zenodo.42002) 

# virus_identification_tools_benchmarking

## Quickstart

1. Grab the code
```
$ git clone git@github.com:MGXlab/virus_identification_tools_benchmarking.git 
$ conda create -n virbench --file conda-linux-64.lock
```

2. Define a tab-separated samplesheet with a header and  column names
  - `sample_id`
  - `pair_id`: microbial and viral paired id
  - `fraction`: `viral` or `microbial` (can be anything really)
  - `R1`: Path to forward fastq file
  - `R2`: Path to reverse fastq file
  - `R1_MD5`: MD5 numbers of Generated R1 FASTQ files
  - `R2_MD5`: MD5 numbers of Generated R2 FASTQ files

3. Fill in the `config.yaml` based on your needs.

4. Execute from within this dir.

```
# This is a dry run
(virbench)$ snakemake -j 32 --use-conda --conda-frontend mamba -p -n
```
* Remove `-n` to run it

## Input

Short, paired-end sequencing reads for the viral and microbial fraction of a 
sample. The `fraction` information must be provided in the samplesheet.

