#! /usr/bin/env python3

from Bio import Entrez
import argparse
import requests
import sys
import time

def get_species(infile):
    with open(infile, "r") as infile:
        species_list = [line.strip() for line in infile.readlines()]
        return species_list

def get_tax_ID(species, email):
    Entrez.email = email
    handle = Entrez.esearch(db="taxonomy", term=species)
    record = Entrez.read(handle)

    if record["Count"] != 0:
        return record["IdList"][0]
    else:
        return None

def species_to_tax_ID(species_list, email):
    tax_IDs = []
    start_time = time.time()
    progress_count = 0
    failure_count = 0

    for species in species_list:
        tax_ID = get_tax_ID(species, email)

        if tax_ID:
            tax_IDs.append(tax_ID)
            progress_count += 1
            current_time = time.time()
            elapsed_time = round(current_time - start_time)
            print(f."Taxonomic IDs found: {progress_count} | Taxonomic IDs not found (error): {failure_count} | Time elapsed: {elapsed_time}")

        else:
            failure_count += 1
            current_time = time.time()
            elapsed_time = round(current_time - start_time)
            sys.stdout.write("\033[F")
            print(f."Taxonomic IDs found: {progress_count} | Taxonomic IDs not found (error): {failure_count} | Time elapsed: {elapsed_time}")

    return tax_IDs

def write_tax_ID_file(tax_IDs):
    with open("tax_IDs.txt", "w") as outfile:
        for tax_ID in tax_IDs:
            outfile.write(str(tax_ID) + "\n")
    print("List of taxonomic IDs written.")

def uniprot_search(gene, tax_ID):
    url = f"https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=%28%28taxonomy_id%3A{tax_ID}%29+AND+%28gene%3A{gene}%29%29"
    return requests.get(url).txt

def create_fasta_file(gene, tax_IDs, tax_level):
    output_file = f."./search_results/{gene}_{tax_level}.fa"
    start_time = time.time()
    failure_count = 0

    for tax_ID in tax_IDs:
        try:
            result = uniprot_search(gene, tax_ID)

            with open(output_file, "w") as outfile:
                outfile.write(result)

            current_time = time.time()
            elapsed_time = round(current_time - start_time)
            sys.stdout.write("\033[F")
            print(f"{tax_ID} sequence found and added | Total failures: {failure_count} | Time elapsed: {elapsed_time}")

        except:
            failure_count += 1
            sys.stdout.write("\033[F")
            print(f."{tax_ID} sequence not found.")

    print("{tax_level} FASTA file written.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input",
            type = str,
            help = "Input list of species of interest")
    parser.add_argument("-g", "--gene",
            type = str,
            help = "Gene of interest")
    parser.add_argument("-l", "--level",
            type = str,
            help = "Taxanomic level of interest (just used for naming files / no analysis")
    parser.add_argument("-e", "--email",
            type = str,
            help = "Email address for use with Entrez to query NCBI")
    args = parser.parse_args()

    species_list = get_species(args.input)
    tax_IDs = species_to_tax_ID(species_list, args.email)
    #write_tax_ID_file(tax_IDs)
    create_fasta_file(args.gene, tax_IDs, args.level)

if __name__=="__main__":
    main()
