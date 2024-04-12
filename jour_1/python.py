print('hello world')

def add(a,b):
    print(a+b)
add(2,3)

def multi(a,b):
    print(a*b)
multi(5,4)

# ecrire une fonction qui convertit la température de Celsius en Fahrenheit et inversement


# def convert(T,type):
#     if(type=='celsius'):
#          T = T+32
#          return T
#     else(type=='fahrenheit')
#         T = T-32
#         return T 

def convert_temp(temp, type):
    if type == 'celsius':
        fahrenheit = (temp * 9/5) + 32
        return fahrenheit
    elif type == 'fahrenheit':
        celsius = (temp - 32) * 5/9
        return celsius
    else:
        print('type de temp intypeide')

conversion = convert_temp(20, 'm')
print (conversion)


string = 'Sauf erreur je ne me trompe jamais !'

print ('Le premier element de la string est :', string[0])

print ('Le dernier element de la string est :', string[-1])

a = 'le prix de mon article est 22 euros'
b = a.find('22')
print(b)