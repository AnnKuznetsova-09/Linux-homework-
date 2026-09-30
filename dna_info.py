import sys
sequence = sys.argv[1]
length = len(sequence)
count_a = sequence.count ("A")
count_t = sequence.count ("T")
count_g = sequence.count ("G")
count_c = sequence.count ("C")
GC = ((count_g + count_c)/length)*100
print(length)
print (count_a)
print(count_t)
print(count_g)
print(count_c)
print(GC)
