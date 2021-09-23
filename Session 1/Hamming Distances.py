import matplotlib.pyplot as plt

DNA_Seqs = []
matrix_Dis = []


def hamming_distances(seq1, seq2):
     mismatches = 0
     for x in range(len(seq1)):
         if seq1[x] != seq2[x]:
             mismatches += 1
     return mismatches

def matrix_distance():
    seq_distance = []
    for i in range(len(DNA_Seqs)):
        for j in range(len(DNA_Seqs)):
           if i == j:
            seq_distance.append(0)
           else:
            seq_distance.append(hamming_distances(DNA_Seqs[i], DNA_Seqs[j]))

        matrix_Dis.append(seq_distance)
        seq_distance = []


def read_seq():
    seq_num = int(input("Enter seqs num : "))

    for x in range(seq_num):
       seq = input("Enter " + str(x+1) + " seq : ")
       DNA_Seqs.append(seq)


read_seq()

matrix_distance()


for x in range(len(matrix_Dis)):
    print(matrix_Dis[x], sep="\n")


plt.imshow(matrix_Dis, cmap='hot', interpolation='nearest')
plt.show()

