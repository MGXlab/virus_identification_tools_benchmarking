import sys
import numpy as np
import pandas as pd
from Bio import SearchIO
import argparse
import multiprocessing

# Create an argument parser object
parser = argparse.ArgumentParser(description='Example script')

# Add the -in and -out options
parser.add_argument('-in', dest='input_file', help='Input file', required=True)
parser.add_argument('-out', dest='output_file', help='Output file', required=True)
# Add the --threads option
parser.add_argument('-t', dest='num_threads', type=int, help='Number of threads', required=True)

# Parse the command line arguments
args = parser.parse_args()

# Get the input file name and output file name from the arguments
input_file = args.input_file
output_file = args.output_file
# Get the number of threads from the arguments
num_threads = args.num_threads

d = []
with open(input_file, 'r') as fin:
    for record in SearchIO.parse(fin, "hmmsearch3-domtab"):
        for hit in record.hits:
            for hsp in hit.hsps:
                d.append(
                    {
                        'contig_id': hit.id,
                        'hmm': record.id ,
                        'bitscore': hit.bitscore,
                        'hit_start': hsp.hit_start,
                        'hit_end': hsp.hit_end,
#                         'hit_length': (hsp.hit_end - hsp.hit_start)*3
                    })

f = pd.DataFrame(d)
f['contig_id'] = f['contig_id'].map(lambda x: str(x)[:-2])
f.to_csv(output_file, sep='\t',index=False)
