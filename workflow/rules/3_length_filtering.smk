rule length_filter:
    input:
        scaffolds_header_fixed = rules.scaffolds_header_fix.output.scaffolds_header_fixed
    output:
        scaffolds_length_filtered = "results/{fraction}/{sample}/scaffolds/{sample}_scaffolds_gt1500.fasta"
    params:
        length = config["SEQTK"]["length"]
    conda:
        "../envs/seqtk.yaml"
    shell:
        "seqtk seq -L {params.length} {input.scaffolds_header_fixed} > {output.scaffolds_length_filtered}"