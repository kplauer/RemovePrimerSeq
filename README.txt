PROJECT TITLE: primer_remove.py 
PURPOSE: CLASSWORK - Supplemental code needed to complete Metagenomics Final Project
	 Allows user to remove known primer sequence from .fa seq data
         This code is still in draft form and could be improved in multiple ways 
         (i.e. it will only accept fasta files with the extensions .fa and .gz and takes a lot of time with large meta- files)
         The intent of this code was in a multi-step pipeline which did not req further improvements at that time 

DATE: Nov 29, 2016
HOW TO RUN: Tested using Python 3.4.0

    Example:
        $ primer_remove.py --file_name=/path/to/some.fa --primer_file=/path/to/some/file.txt --output_file=output_file.fa --stat_report=stats
        This will take a fasta file, the primer sequences found in the primer file and output it to a new fasta file with the primers sequence removed
        Output files:  
		1. revised fasta file with primer sequence removed from reads
                2. stat file saying # of reads total and the # of reads that had primer sequence removed            		

    Required Command Line Arguments: 
        --file_name or -f
        --primer_file or -p
        --output_file or -o
                                     
AUTHOR: Kim Lauer
FURTHER INSTRUCTIONS:
        primer file should contain primers sequences on seperate line
