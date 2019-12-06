import re
class Comparison:
    def __init__(self):
        self.content82=''
        self.content98 = ''
    def extract(self):
        file_handler82 = open("Mus_musculus.GRCm38.82.chr.gtf", "r+")
        file_handler82.readline()
        file_handler82.readline()
        file_handler82.readline()
        file_handler82.readline()
        file_handler82.readline()
        self.content82 = file_handler82.read()
        file_handler98 = open("Mus_musculus.GRCm38.98.chr.gtf", "r+")
        file_handler98.readline()
        file_handler98.readline()
        file_handler98.readline()
        file_handler98.readline()
        file_handler98.readline()
        self.content98 = file_handler98.read()
    def notIn98(self):
        line82 = self.content82.split("\n")
        tabDelimitedInput82 = []
        for ex in line82:
            if ex.__contains__('	exon	'):
                var = ex.split('\t')
                chromosome = var[0]
                start = var[3]
                end = var[4]
                strand = var[6]
                typeFinder = re.findall('gene_biotype "\S+', ex)[0][14:]
                typeFinder2 = typeFinder[0:-2]
                geneNameFinder = re.findall('gene_name "\S+', ex)
                geneNameFinder = str(geneNameFinder).replace('[', '').replace(']', '').replace('\'', '').replace('gene_name ', '').replace('\"', '').replace(';', '')
                transcriptIDFinder = re.findall('ENSMUST[0-9]{11}', ex)
                transcriptIDFinder = str(transcriptIDFinder).replace('[', '').replace(']', '').replace('\'', '')
                geneIDFinder = re.findall('ENSMUSG[0-9]{11}', ex)
                geneIDFinder = str(geneIDFinder).replace('[', '').replace(']', '').replace('\'', '')
                exonIDFinder = re.findall('exon_id "\S+', ex)
                exonIDFinder = str(exonIDFinder).replace('[', '').replace(']', '').replace('\'', '').replace('exon_id ', '').replace('\"', '').replace(';', '')
                tabDelimitedInput82.append(transcriptIDFinder + '\t' + geneIDFinder + '\t' + geneNameFinder + '\t' + typeFinder2 + '\t' + chromosome + '\t' + strand + '\t' + exonIDFinder + '\t' + start + '\t' + end)
        line98 = self.content98.split("\n")
        tabDelimitedInput98=[]
        for ex in line98:
            if ex.__contains__('	exon	'):
                var = ex.split('\t')
                chromosome = var[0]
                start = var[3]
                end = var[4]
                strand = var[6]
                typeFinder = re.findall('gene_biotype "\S+', ex)[0][14:]
                typeFinder2 = typeFinder[0:-2]
                geneNameFinder = re.findall('gene_name "\S+', ex)
                geneNameFinder = str(geneNameFinder).replace('[', '').replace(']', '').replace('\'', '').replace('gene_name ', '').replace('\"', '').replace(';', '')
                transcriptIDFinder = re.findall('ENSMUST[0-9]{11}', ex)
                transcriptIDFinder = str(transcriptIDFinder).replace('[', '').replace(']', '').replace('\'', '')
                geneIDFinder = re.findall('ENSMUSG[0-9]{11}', ex)
                geneIDFinder = str(geneIDFinder).replace('[', '').replace(']', '').replace('\'', '')
                exonIDFinder = re.findall('exon_id "\S+', ex)
                exonIDFinder = str(exonIDFinder).replace('[', '').replace(']', '').replace('\'', '').replace('exon_id ', '').replace('\"', '').replace(';', '')
                tabDelimitedInput98.append(transcriptIDFinder + '\t' + geneIDFinder + '\t' + geneNameFinder + '\t' + typeFinder2 + '\t' + chromosome + '\t' + strand + '\t' + exonIDFinder + '\t' + start + '\t' + end)
        tabDelimitedInput98=set(tabDelimitedInput98)
        tabDelimitedInput82=set(tabDelimitedInput82)
        print(len(tabDelimitedInput82))
        print(len(tabDelimitedInput98))
        setOfNotIn82 = tabDelimitedInput82.difference(tabDelimitedInput98)
        print(len(setOfNotIn82))
        setOfNotIn98 = tabDelimitedInput98.difference(tabDelimitedInput82)
        print(len(setOfNotIn98))

def main():
    comp = Comparison()
    comp.extract()
    comp.notIn98()
    # with open('Comparison.txt', 'w') as f:
    #     f.write()
if __name__ == "__main__":
    main()
