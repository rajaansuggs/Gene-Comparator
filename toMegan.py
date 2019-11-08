frequency_matrix = np.zeros((4, len(transcriptBindingFact[0])), dtype=np.int)
        base2index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        for dna in transcriptBindingFact:
            for index, base in enumerate(dna):
                frequency_matrix[base2index[base]][index] += 1
        print(frequency_matrix)
        return frequency_matrix
