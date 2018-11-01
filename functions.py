def getEvenNumbers(n):
    """
    :param n: int
    :return: list of even numbers till n
    """
    if type(n) != int:
        output = 'please enter integer as input'
    else:
        # output = list(filter(lambda x: x%2 ==0 , list(range(n))))
        output = []
        for i in range(n):
            if i%2 == 0:
                output.append(i)
            else:
                pass
    return output

print(getEvenNumbers('nakul'))

#use of map
k = [1,2,3,4,5,6]
# i want to add 2 to every elemt
new_k = []
for element in k:
    new_k.append(element*2)
new_k = list(map(lambda x: x+2, k))

#use of filter
k = [1,2,3,4,5,6]
# i want only odd numbers
new_k = list(filter(lambda x: x%2 != 0, k))


#product
k = [3,4,5,6,7]
product = 1  #x
for element in k: #y
    product = product*element
        # x =  x*y
 product = reduce(lambda x,y : x*y,k)


