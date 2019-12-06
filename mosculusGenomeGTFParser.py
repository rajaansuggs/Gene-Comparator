import re


class GeneAnnotationComparison:

    def __init__(self, fileName):
        """
    This is the constructor that takes in the first and second file
        :param file1Name: first file
        :param file2Name: second file
        """
        self.GTFFileName = fileName
        self.content = ''

    def extract(self):
        """
        This method reads the GTF Files
        """
        file_handler = open(self.GTFFileName, "r+")
        file_handler.readline()
        file_handler.readline()
        file_handler.readline()
        file_handler.readline()
        file_handler.readline()
        self.content = file_handler.read()

    def getCategories(self):
        """
        This method gets each category
        :return:
        """
        listOfDuplicateCategories = []
        categoryFinder = re.findall('gene_biotype "\S+', self.content)
        for parts in categoryFinder:
            listOfDuplicateCategories.append(parts[14:len(parts) - 2])
        listOfCategories = []
        li = [[x, listOfDuplicateCategories.count(x)] for x in set(listOfDuplicateCategories)]
        string = str(li).replace(']','</td></tr>\n').replace('\'','').replace(',','').replace('[[','<tr><td>').replace('[','<tr><td>')
        li1=string.split('\n')
        newLI=[]
        for i in li1:
            newLI.append(i.lstrip().replace(' ', '</td><td>'))
        l=str(newLI).replace(',','\n').replace('[','').replace(']','').replace('\'','')
        print(l)
        for i in listOfDuplicateCategories:
            if i not in listOfCategories:
                listOfCategories.append(i)
        return listOfCategories

    def getCount(self):
        """
        This method gets the count for each category
        :return: di (a dictionary of category as keys and counts as values)
        """
        di = dict()
        listOfDuplicateCategories = []
        categoryFinder = re.findall('gene_biotype "\S+', self.content)
        for parts in categoryFinder:
            listOfDuplicateCategories.append(parts[14:len(parts) - 2])
        for p in listOfDuplicateCategories:
            if p in di:
                di[p] = di[p] + 1
            else:
                di[p] = 1
        return di

    def getAssociations(self):
        """
        Writes an association between category and number file
        """
        line = self.content.split("\t")
        result = []
        for i in line[:-1]:
            var = re.findall('gene_biotype "\S+', i)[0][14:]
            result.append(var[0:-2] + " " + i[0:2])
        r = '\n'.join(map(str, result))
        with open('associationsBetweenCategoryAndNumber', 'w') as f:
            f.write(r)

    def getGeneNames(self):
        """
        This method gets the gene names
        :return: listOfDuplicateCategories
        """
        listOfDuplicateCategories = set()
        geneNameFinder = re.findall('gene_name "\S+?;', self.content)
        for parts in geneNameFinder:
            listOfDuplicateCategories.add((parts[11:len(parts) - 2]))
        return listOfDuplicateCategories
        print(listOfDuplicateCategories)

    def numberOfTranscripts(self):
        """
        This method prints the number of annotated transcripts
        """
        transcript = re.findall('	transcript	', self.content)
        print('Number of transcripts annotated', len(transcript))

    def createTranscriptTabDelimitedInput(self):
        """
        This method returns the necessary information such as chromosome, start, end, strand, gene name, id, exon id, transcript id and type in a tabbed string called tabFileInput
        :return: tabDelimitedFile
        """
        line = self.content.split('\n')
        tabDelimitedInput = []
        for ex in line:
            if ex.__contains__('	exon	'):
                var = ex.split('\t')
                chromosome = var[0]
                start = var[3]
                end = var[4]
                strand = var[6]
                typeFinder = re.findall('gene_biotype "\S+', ex)[0][14:]
                typeFinder2 = typeFinder[0:-2]
                geneNameFinder = re.findall('gene_name "\S+', ex)
                geneNameFinder = str(geneNameFinder).replace('[', '').replace(']', '').replace('\'', '').replace(
                    'gene_name ', '').replace('\"', '').replace(';', '')
                transcriptIDFinder = re.findall('ENSMUST[0-9]{11}', ex)
                transcriptIDFinder = str(transcriptIDFinder).replace('[', '').replace(']', '').replace('\'', '')
                geneIDFinder = re.findall('ENSMUSG[0-9]{11}', ex)
                geneIDFinder = str(geneIDFinder).replace('[', '').replace(']', '').replace('\'', '')
                exonIDFinder = re.findall('exon_id "\S+', ex)
                exonIDFinder = str(exonIDFinder).replace('[', '').replace(']', '').replace('\'', '').replace('exon_id ','').replace('\"', '').replace(';', '')
                tabDelimitedInput.append(
                    transcriptIDFinder + '\t' + geneIDFinder + '\t' + geneNameFinder + '\t' + typeFinder2 + '\t' + chromosome + '\t' + strand + '\t' + exonIDFinder + '\t' + start + '\t' + end)
        tabFileInput = '\n'.join(tabDelimitedInput)
        return tabFileInput

    def createGeneTabDelimitedInput(self, version):
        """
        This method generates a tab delimited string containing necessary information such as chromosome, gene id, start, end, gene name, transcript id, version and transcrpt number
        :param version: The genome gtf version (1 for musculus 82, 2 for musculus 98)
        :return: tabFileInput
        """
        line = self.content.split('\n')
        tabDelimitedInput = []
        for ex in line:
            if ex.__contains__('	transcript	'):
                var = ex.split('\t')
                chromosome = var[0]
                start = var[3]
                end = var[4]
                transcriptNumberFinder = re.findall('transcript_version "\S+', ex)
                transcriptNumberFinder = str(transcriptNumberFinder).replace('\"', '').replace(';', '')
                geneNameFinder = re.findall('gene_name "\S+', ex)
                geneNameFinder = str(geneNameFinder).replace('[', '').replace(']', '').replace('\'', '').replace(
                    'gene_name ', '').replace('\"', '').replace(';', '')
                transcriptIDFinder = re.findall('ENSMUST[0-9]{11}', ex)
                transcriptIDFinder = str(transcriptIDFinder).replace('[', '').replace(']', '').replace('\'', '')
                geneIDFinder = re.findall('ENSMUSG[0-9]{11}', ex)
                geneIDFinder = str(geneIDFinder).replace('[', '').replace(']', '').replace('\'', '')
                tabDelimitedInput.append(
                    chromosome + '\t' + geneIDFinder + '\t' + start + '\t' + end + '\t' + geneNameFinder + '\t' + transcriptIDFinder + '\t' + str(
                        version) + '\t' + transcriptNumberFinder)
        tabFileInput = '\n'.join(tabDelimitedInput)
        return tabFileInput

def main():
    """
    This is the main method
    """
    # =============================================File of Genome Version 82
    fileOfGenomeVersion82 = "Mus_musculus.GRCm38.82.chr.gtf"
    mouseGenomeVersion82 = GeneAnnotationComparison(fileOfGenomeVersion82)
    mouseGenomeVersion82.extract()
    m82 = mouseGenomeVersion82.getCategories()
    print("There are " + str(len(m82)) + " categories in Mus_musculus.GRCm38.82.chr.gtf")
    for m in m82:
        print(m)
    mouseGenomeVersion82.getGeneNames()
    categoryCount = str(mouseGenomeVersion82.getCount())
    categoryCount = categoryCount.replace('{', '')
    categoryCount = categoryCount.replace(':', '\t')
    categoryCount = categoryCount.replace(',', '\n')
    categoryCount = categoryCount.replace('\'', '')
    categoryCount = categoryCount.replace('}', '')
    with open('countForEachCategory', 'w') as f:
        f.write(categoryCount)
    mouseGenomeVersion82.numberOfTranscripts()
    tabDelimitedList = mouseGenomeVersion82.createTranscriptTabDelimitedInput()
    tabGeneDelimitedList = mouseGenomeVersion82.createGeneTabDelimitedInput(82)
    print("\n\n\n")
    # =============================================File of Genome Version 98
    fileOfGenomeVersion98 = "Mus_musculus.GRCm38.98.chr.gtf"
    mouseGenomeVersion98 = GeneAnnotationComparison(fileOfGenomeVersion98)
    mouseGenomeVersion98.extract()
    m98 = mouseGenomeVersion98.getCategories()
    print("There are " + str(len(m98)) + " categories in Mus_musculus.GRCm38.98.chr.gtf")
    for m in m98:
        print(m)

    mouseGenomeVersion98.numberOfTranscripts()
    tabDelimitedList2 = mouseGenomeVersion98.createTranscriptTabDelimitedInput()
    tabGeneDelimitedList2 = mouseGenomeVersion98.createGeneTabDelimitedInput(98)
    with open('Transcript.txt', 'w') as f:
        f.write(tabDelimitedList +'\t'+tabDelimitedList2)
    with open('Gene82.txt', 'w') as f:
        f.write(tabGeneDelimitedList)
    with open('Gene98.txt', 'w') as f:
        f.write(tabGeneDelimitedList2)

if __name__ == "__main__":
    main()
