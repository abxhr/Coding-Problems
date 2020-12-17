import numpy
n_m = list(map(int, input().split())) 
lst = []
for i in range(n_m[0]):
    lst.append(list(map(int, input().split())))
lst = numpy.array(lst)
print(numpy.transpose(lst))
print(lst.flatten())