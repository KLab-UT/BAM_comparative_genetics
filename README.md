# BamA Comparative Genetics

The purpose of this project is to analyze the conservation of the protein BamA and its
satellite POTRA domains.

## Abstract

$\beta$-barrel assembly machinery (BAM) is a protein complex vital to cell
survival in gram-negative bacteria that functions to insert proteins into the
cell’s outer membrane. BamA, a protein composed of a membrane-bound beta barrel
and several potra domains that protrude into the cytosol, is the primary subunit
within BAM. It is suggested that BamA is conserved due to its widespread
presence across the bacterial tree of life. Here we quantify the conservancy of
BamA in 142 species of gram-negative bacteria from across the bacterial tree of
life, with a focus on 120 species belonging to the order Enterobacterales. In
addition, we compared the conservancy of BamA with other proteins with high and
moderate levels of conservation in Enterobacterales. Lastly, we discuss regions
of BamA that are of high conservation in the context of their potential as
antibiotic targets.

## Methods

### Scripts

* fasta_cross.py (ALEX GET BACK TO THIS ONE)

* e_coli_farm.py takes a multiple sequence alignment FASTA file and "farms" the
  alignment for anything not present in a given species (default for this
  project is *Escherichia coli*)
  * Removes all columns not represented by target species
    * Eliminates gaps in target species and adjusts all other amino acid
      sequences
  * Writes farmed sequences to new FASTA file

* position.py creates the Position class to calculate particular statistics at
given positions along the amino acid sequence alignment. Such statistics include
  * Sample Size: Number of amino acids present at a given position, excluding
    gaps
  * Unique Amino Acids: The number of unique amino acids represented at the given
    position
  * Proportion: The proportion of the most common amino acid to the total
    amount of amino acids found at a given position

* stat.py takes a multiple sequence alignment FASTA file and tracks statistics
provided by the Position class across the entire alignment, writing them to CSV
files.
  * Removes significant gaps from alignments
  * Makes note of positions that are significantly conserved
    * Expecting the protein to be fairly well conserved amongst different taxa,
      though less and less the farther back in the phylogenetic distance we reach
    * Expecting the protein to be highly conserved just in Enterobacterales

* analysis_plot.r takes a CSV file with statistics about position objects and
  turns them into histogram & box and whisker plots before saving them into PNG
  files
   * \*_histogram.png
     * Histogram plot
     * Positions at or above 98% conservation are color coded red
   * \*_box.png
     * Includes box and whisker plots & violin plots

### Pipeline

![alt text](Pipeline.png "Script Pipeline for Data")
