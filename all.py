# Variables
# int, str,l float, bool
x = 9
x = str(x)
x = float(x)
# tuple, list(arrays)

tup = ('machine', 'learning')
list_1 = ['machine', 'learning']
list_1[0] = list_1[0]+'s'
# tup[0] = tup[0]+'s'
# TypeError: 'tuple' object does not support item assignment
list_2 = ['class']
tup_2 = ('class')
list_3 = list_1+list_2
print(list_3)
tup_3 = (tup,tup_2)
print(tup_3)


#list to tuple
print(tuple(list_3))


# math functions
x = 9.879787686765876
#round
print(round(x,2))
#math
import math #pip install math

print(math.ceil(x))
print(math.floor(x))

y = []
#append
y.append(1)
y = [1,4,2,5,3,5,7]

#navigating a list
y[3]
y[-1]
y[2:4]

print(len(y))
print(max(y))
print(min(y))
# print(cmp())  # comparing two tuples

# comparing two variables
a = 10
b = 90*8
print(a == b)

# square root
print(math.sqrt(100))


a = 0  #int
a = 98.0  #float
int(a)


# declaring gloabal
# global a

#multi dimensional lists
number_list = [[1,2,3,4],[5,6,7,8]]
# [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]

# Boolean operators

k = (5 > 6) and (0 == 0)
print(k)

k = (5 > 6) or (0 == 0)
print(k)

print(not(5 > 6))

#machinelearning098@gmail.com
# machine@123

# dictionary
new_dictionary = {}
new_dictionary = {'os': 'linux', 'version': 3.5}
print(new_dictionary.keys())
print(new_dictionary.values())
print(new_dictionary['os'])
new_dictionary['flavor'] = 'Debian'
print(new_dictionary)
del new_dictionary['flavor']
print(new_dictionary)
new_dictionary = {}



# Data Frames
# series



