import re
class GeneAnnotationComparison:

    def __init__(self, fileName):
        """
    This is the constructor that takes in the first and second file
        :param file1Name: first file
        :param file2Name: second file
        """
        self.GTFFileName = fileName
        self.content=''
    def extract(self):
        file_handler = open(self.GTFFileName, "r+")
        file_handler.readline()
        file_handler.readline()
        file_handler.readline()
        file_handler.readline()
        file_handler.readline()
        self.content = file_handler.read()
    def getCategories(self):
        listOfDuplicateCategories=[]
        categoryFinder=re.findall('gene_biotype "\S+', self.content)
        for parts in categoryFinder:
            listOfDuplicateCategories.append(parts[14:len(parts)-2])
        listOfCategories=[]
        for i in listOfDuplicateCategories:
            if i not in listOfCategories:
                listOfCategories.append(i)
        return listOfCategories

    def transcriptFinder(self):
        listOfDuplicateCategories=[]
        categoryFinder = re.findall('gene_biotype "\S+', self.content)
        for parts in categoryFinder:
            listOfDuplicateCategories.append(parts[14:len(parts) - 2])
        transcriptFinder = re.findall('ENSMUST\S+', self.content)
        parsedtranscriptFinder=[]
        for i in transcriptFinder:
            parsedtranscriptFinder.append(i[:-2])
        print(self.merge(listOfDuplicateCategories, parsedtranscriptFinder))

    def merge(self, list1, list2):
        mergedList = []
        for m in range(max(len(list1), len(list2))):
            while True:
                try:
                    tup =(list1[m], list2[m])
                except IndexError:
                    if len(list1)>len(list2):
                        list2.append('')
                        tup = (list1[m], list2[m])
                    elif len(list1)<len(list2):
                        list1.append('')
                        tup = (list1[m], list2[m])
                    continue
                mergedList.append(tup)
                break
        return mergedList

    def getAssociations(self):
        line = self.content.split("\t")
        listOfDuplicateCategories = []
        categoryFinder = re.findall('gene_biotype "\S+', self.content)
        for parts in categoryFinder:
            listOfDuplicateCategories.append(parts[14:len(parts) - 2])
        listOfCategories = []
        for i in listOfDuplicateCategories:
            if i not in listOfCategories:
                listOfCategories.append(i)

        for c in listOfCategories:
            for l in line:
                if c in l:
                    print(c)
    def getGeneNames(self):
        listOfDuplicateCategories = []
        geneNameFinder = re.findall('gene_name "\S+', self.content)
        for parts in geneNameFinder:
            listOfDuplicateCategories.append(parts[11:len(parts) - 2])
        g=[]
        for i in listOfDuplicateCategories:
            if i not in g:
                g.append(i)
        print(g)
def main():
    """
    This is the main method
    """
    fileOfGenomeVersion82="Mus_musculus.GRCm38.82.chr.gtf"
    mouseGenomeVersion82 = GeneAnnotationComparison(fileOfGenomeVersion82)
    mouseGenomeVersion82.extract()
    mouseGenomeVersion82.transcriptFinder()
    m82 = mouseGenomeVersion82.getCategories()
    print("There are "+str(len(m82))+" categories in Mus_musculus.GRCm38.82.chr.gtf")
    for m in m82:
         print(m)
    mouseGenomeVersion82.getGeneNames()
    print("\n\n\n")
    fileOfGenomeVersion98 = "Mus_musculus.GRCm38.98.chr.gtf"
    mouseGenomeVersion98 = GeneAnnotationComparison(fileOfGenomeVersion98)
    mouseGenomeVersion98.extract()
    m98 = mouseGenomeVersion98.getCategories()
    print("There are " + str(len(m98)) + " categories in Mus_musculus.GRCm38.98.chr.gtf")
    for m in m98:
        print(m)
if __name__ == "__main__":
    main()
