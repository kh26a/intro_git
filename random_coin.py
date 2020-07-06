import numpy.random as rd
dict = {0:0, 1:0, 2:0, 3:0, 4:0}
for i in range(100):
	n = rd.randint(low=0, high=2, size=4).sum()
	dict[n] += 1
print(dict)
