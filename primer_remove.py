#!/usr/bin/env python3
# Kim Lauer (klauer2)
# 11/29/16
# Find and remove primer sequences from sequence reads
# Draft 1 - not optimized

import argparse
import re
import gzip

# variables
count = 0
primerList = []
#if stat file selected, prints out number of reads primer removed from
stats = {'total_reads':0, 'reads_revised':0}


# Parsing of Fasta files
def fasta(file_open, primerList, primer_count):
    line_count = 0
    match = False
    f = open(output_file, 'a')
    # loop thru file line by line
    for line in file_open:
        line_count = line_count + 1
        count = primer_count
        # finds number of peptides
        if line.startswith('>'):
            stats['total_reads'] += 1
            f.write(line)
        # finds if sequence matches
        else: 
            while count > 0:
                primer = primerList[count-1]
                temp = "(.*)(" + primer + ")(.*)"
                temp_search = re.search(temp, line)
                count = count - 1
                if (temp_search):
                    stats['reads_revised'] += 1
                    line = (temp_search.group(1) + temp_search.group(3) + "\n")
            f.write(line)
    f.close()

# parses the command line to obtain file name from user
parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file_name', required=True,  help="Required - Enter file name with path")
parser.add_argument('-p', '--primer_file', required=True, help="Required - Enter primer file with sequence names to retrieve")
parser.add_argument('-o', '--output_file', required=True, help="Required - Enter output file for reads with primer sequences removed")
parser.add_argument('-s', '--stat_report', required=False, help="Prints out summary of how many reads revised")

args = parser.parse_args()

file_name = args.file_name
primers = args.primer_file
output_file = args.output_file
stat_report = args.stat_report

primerfile_open = open(primers)

# parses primer file to upload regex expressions for primers
for line in primerfile_open:
    primer_to_list = line.rstrip()
    print(primer_to_list)
    primerList.append(primer_to_list)

# closes primer file once uploaded into list
primerfile_open.close()

# checks if file is a zip file & opens file in text mode
if (file_name.endswith('.gz')):
    file_open = gzip.open(file_name, 'rt')
else:
    file_open = open(file_name)

num_of_primers = len(primerList)
print(str(num_of_primers))

if (file_name.endswith('.fa')):
    fasta(file_open, primerList, num_of_primers)
else:
    print("File does not end with .fa")

if stat_report is not None:
    s = open(stat_report, 'a')
    s.write("Results of removing primer sequences\n")
    s.write("Total input reads: {0}\n".format(stats['total_reads']))
    s.write("Reads modified to remove primer: {0}\n".format(stats['reads_revised']))
    s.close() 


