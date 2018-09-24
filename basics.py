k = 98
if k%2 == 0:
    print(str(k)+' is even number')
else:
    print(str(k)+' is odd number')



def check_even(k):
    try:
        if k%2==0:
            return str(k)+' is even number'
        else:
            return str(k)+' is odd number'
    except IndentationError as e:
        print(' please select integer or float to return')
    except IndexError as ee:
        print('Index error')
    except:
        print('its error')

# print(check_even('bhfh'))

def check_even_odd(k):
    if type(k) not in ['int','float']:
        print('its not an integer or float')
    else:
        print(k)

# check_even_odd('98')


user_age = 28
print(user_age == str)

sentence = 'this is class'
sentence[0]
sentence[-1]
len(sentence)
for i in sentence:
    print(i)
    print(type(i))

k = [1,2,3,'nakul']
for element in k:
    print(element)
    print(type(element))

for element in range(len(k)):
    if element%2 == 0:
        print(k[element])
    else:
        pass

even_pos = []

type(k)
k[:3]
k[0:3]
k[1:3]
k[-1]
k[2:-1]
len(k)



sentence = 'this is class'
#Upper case
print(sentence.upper())
#lower case
print(sentence.lower())


#Find
print(sentence.find(' is'))
print(sentence.find('is',4))
#replace
print(sentence.replace(" is", " was"))
#slicing
print(sentence[0])
print(sentence[:4])
print(sentence[2:5])

#splitting
sentence = 'this is class'
k = 6
print(sentence.split())

#user input
k = input("please enter text")


#Assignment
'''
create find_nth_pos() 
find_nth_pos(sentence,substr,pos)
count = 0
if pos == 0
return sentence.find(substr)

sentence.find(substr,sentence.find(substr)+1)

for i in range(pos):
 sentence = sentence[sentence.find(substr)+1:]
sentence.find(substr)
'''

def find_n_th(sentence,substr,pos):
    if pos == 0:
        return sentence.find(substr)

    else:
        count = 0
        for i in range(pos):
            start_pos = sentence.find(substr)+1
            count = count+len(sentence[:start_pos])
            sentence = sentence[start_pos:]
        return count+sentence.find(substr)

pos = find_n_th(sentence,'is',2)