P = '''John said: 'let's learn python together'.'''
print(P)

x = 0.2 + 0.2
print(x)
print(x==0.4)

import math
f= 0.2 + 0.2 + 0.2
print(f)
print(math.isclose(f,0.6))

print(1 < 2)

d = 1
xstr = '1'
test = d == xstr
print(test)
print(type(test))

print(3+2)

print('3'+'2')

a='3'+'2'
print(type(a))

import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')                              # (7)

y ='abc'.upper()
print(y)

x = 'ACBtasDFfa'.lower()
print(x)

'Hi'.center(40)

'Hi'.center(40,'#')

a = False
b = 7
print(f'the value of a is {a} and the value of b is {b}')

a = False
b = 7
print('the value of a is {} and the value of b is {}'.format(a,b))

x = str('abc')
xup = str.upper(x)
print(xup)

width = 33
length = 56
height = 30.5
box_volume = width * length * height
print(box_volume)
print(f'the volume of the box is {box_volume} cubic centimeter')

lst = [1,2,2,'zero',3]
print(lst)

t= type(lst)
print(t)

my_list = ['first','second','third','fourth','fifth']
print(my_list[4])

print(my_list[0])

print(my_list[-1])

print(my_list[-5])

print(my_list[0:4])

print(my_list[-4:-2])

list.append(my_list,'sixth')
print(my_list)
my_list.remove('third')
print(f'lst after removing the first third is {my_list}')

my_list.pop(2)
print(f'lst after removing index 2 is {my_list}')

my_list.pop()
print(f'lst after removing index is {my_list}')

my_list.reverse()
print(my_list)

a ="welcome to the class"
x= a.split()
print(x)





line ='from firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
domain = line.split()[1].split('@')[1]
print(domain)

a,b,c = 1, True, "word"
print(f'in this case a equal to {a},b equal to {b}, and c equal to {c}')

w = "What"
i = "IS"
c = "CamelCase?"
x= '{}，{}，{}'，format(w,i.lower,c)
print(x)

x= f'{w},{i},{c}'
print(x)

x='{} {} {}'.format(w,i.lower(),c)
print(x)


x=1
y=2
y=x
x=y
test = x == 2
print(test)

asx_value = 7111.4
date = '2021-01-25'
units = 1
currency = 'AUD'

x = f'the closing value of {units} of all ordinaries on {date} was {asx_value} {currency}.'
print(x)

# Downloads Qantas share price beginning 1 January 2020
import yfinance
tic = "QAN.AX"
start = '2020-01-01'
df = yfinance.download(tic, start, None)
print(df)
df.to_csv('qan_stk_prc.csv')


# Downloads Qantas share price beginning 1 January 2020
import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end)
print(df)
df.to_csv('qan_stk_prc.csv')


# Downloads Qantas share price beginning 1 January 2020
import yfinance as df
df.download("QAN.AX", '2020-01-01', None).to_csv('qan_stk_prc.csv')

import json
help(json.load)

b = 'problem'
a = f'this is called {b}'
a = f'{a} parsons {b}'
b = print
b(a)


t =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(t[-8:])

print(t[-8:10])

print(t[-7:])

print(t[2:10])

print(t[-8:12])

print(t[:5])

print(t[:-5])

print(t[-9:-6])

print(t[1:4])


dic0 = {'a': 1, 'b': 2, 'c': 3}
dic1 = dic0.update({'a': 0, 'd': 4})
x = dic0['a']
print(x)

dic0 = {'a': 1, 'b': 2, 'c': 3}
dic1 = dic0.update({'a': 0, 'd': 4})
print(dic0)


list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']
sol = list_a[1:7]
print(sol)
sol.remove('bad')
sol.append('including')
sol.insert(3,'good')
sol.extend(list_b)
print(sol)

f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
f_suburbs.remove("Randwick")
f_suburbs.remove("Kensington")
f_suburbs.add('Fairfield')
f_suburbs.add('Fairfield East')
f_suburbs.add('Fairfield Heights')
f_suburbs.add('Fairfield West')
f_suburbs.add('Fairlight')
f_suburbs.add('Fiddletown')
f_suburbs.add('Five Dock')
f_suburbs.add('Forest Glen')
f_suburbs.add('Forest Lodge')
f_suburbs.add('Forestville')
f_suburbs.add('Freemans Reach')
f_suburbs.add('Freshwater')
print(f_suburbs)

current = (21+13)
last = (13)
print(f'The 10th element in the sequence is {current},the 8th element would be {last}.')



f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
f_suburbs.pop("Randwick")
f_suburbs.pop("Kensington")

f_suburbs1 = f_suburbs.update({'Fairfield': 18081,'Fairfield East': 5273,'Fairfield Heights':7517,'Fairfield West':11575,'Fairlight':5840,'Fiddletown':233,'five dock':9356,'Forest Glen':None,'Forest Lodge':4583,'Forestville': 8329,'Freemans Reach':1973,'Freshwater':8866})
print(f_suburbs)

