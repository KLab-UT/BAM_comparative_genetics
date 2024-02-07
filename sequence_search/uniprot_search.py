import requests
import random
import fasta_cross
import sys
import time

# Pulls gene names from ecoli names file. Returns names as list
def get_genes(inFile):
    with open(inFile,'r') as file:
        geneList = [i.split()[0] for i in file.readlines()]
        return(geneList)


def uniprotSearch(gene,taxID):
    url = f'https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=%28%28taxonomy_id%3A{taxID}%29+AND+%28gene%3A{gene}%29%29'
    return requests.get(url).text

def write_searches(gene):
    for gene in randomSample:
        with open(f'./search_results/{gene}_enterobacterales.fasta','w') as outFile:
            outFile.write(uniprotSearch(gene))

def cross_fasta(names_fasta,search_fasta,write_handle):
    crosser = fasta_cross.Fasta_cross()
    crosser.get_names(names_fasta,'alex') # enterobacterales.fa
    crosser.cross_ref(search_fasta,crosser.bacteria_names,repeat=False)
    crosser.write_fasta(crosser.match_records,handle = write_handle)
    # Skipping the align step for now to save time
    #crosser.align(write_handle,write_handle=write_handle)


def main():
    # All genes in E.coli
    geneList = get_genes('ecoli_all_proteins.txt')

    # uncomment for random Sampling WITHOUT Replacement 
    #geneList = random.sample(geneList, k=10)

    # uncomment for target genes
    #geneList = ['bamA','secY']

    taxID = 561

    #taxIDs of interest
    #------------------
    #Escherichia: 561
    #Enterobacterales: 91347

    totalGenes = len(geneList)
    progressCount = 0
    failureCount = 0
    startTime = time.time()

    print(f'{progressCount}/{totalGenes} searched')
    for gene in geneList:
        try:
            write_handle = f'./search_results/{gene}_enterobacterales.fasta'
            searchResult = uniprotSearch(gene,taxID) 
            with open(write_handle,'w') as outFile:
                    outFile.write(searchResult)

            cross_fasta(
                    names_fasta = 'enterobacterales.fa',
                    search_fasta = write_handle, 
                    write_handle = write_handle
                    )

            progressCount += 1
            currentTime = time.time()
            elapsedTime = round(currentTime - startTime)

            sys.stdout.write("\033[F")
            print(f'{progressCount}/{totalGenes} searched.Time elapsed: {elapsedTime} s. Search Failures {failureCount}')
        except:
            failureCount += 1
            print(f'Search Failures: {failureCount}')
if __name__ == '__main__':
    main()
