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

k = [1,2,3,'nakul']
type(k)
k[:3]
k[0:3]
k[1:3]
k[-1]
k[2:-1]