import yfinance
def qan_tic(): # (1)
 tic = "QAN.AX" # (2)
 return tic # (4)
 print(tic) # (3)

res= qan_tic()
print(res)

def qan_tic(): # (1)
 tic = "QAN.AX" # (2)
 print(tic) # (3)

res = qan_tic() # (5b)
print(res)

# Define a function called `qan_tic`
def qan_tic(): # (1)
 tic = "QAN.AX" # (2)
 print(tic) # (3)
 return tic # (4)
print(qan_tic)

def qan_tic(): # (1)
 tic = "QAN.AX" # (2)
 print(tic) # (3)
 return tic # (4)
print(tic)

def qan_tic(): # (1)
 tic = "QAN.AX" # (2)
 print(tic) # (3)
 return tic # (4)
tic = "WES.AX" # (5)
print(tic) # (6)
qan_tic()

def qan_tic(): # (1)
 print(tic) # (3)
 return tic # (4)
tic = "WES.AX" # (5)
print(tic) # (6)
qan_tic() # (7)

def qan_tic():
 tic = "QAN.AX" # <-- local # (1)
 print(tic) # (2)
 return tic
tic = "WES.AX" # <-- global
qan_tic()

def mk_csv_name(tic): # (1)
 tic = tic.lower() # (2)
 tic_base = tic.split('.')[0] # (3)
 return f'{tic_base}_stk_prc.csv' # (4)
name = mk_csv_name('QAN.AX') # (5)
print(name) # (6)

lst1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]

def even_number_list(lst):
 even = []
 for n in lst:
  if n % 2 == 0:
   even.append(n)
 return even


print( even_number_list(lst1))


evens = [x for x in range(1_000_000 + 1) if x % 2 == 0]
print(evens[:10])

dic = {'a': 1, 'b': 2, 'c': 3}

pairs = []
for key, value in dic.items():
 pairs.append((key,value))
print(pairs)

keys = {key for key in dic}
print(f'The type of {keys} is {type(keys)}')


lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]

def square_root (lst):
 lst_1 = []
 for n in lst:
  n = n**2
  if n > 150:
   lst_1.append(n)
 return lst_1

print(square_root(lst))

lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]

new_lst = [x**2 for x in lst if x**2> 150]
print(new_lst)

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]

numbers_1 =[x for x in set(numbers) if x % 2 == 0]

numbers_1.sort()

print(numbers_1)

s = "This is my test String"
def process_string(s):
 ss = []
 s = s.lower()
 s = s.split()
 ss.append(s)
 return ss

print(process_string(s))


def my_function(x):
 x = x + 1
 return x

x = 3
my_function(x)

print(x)




 def my_function(y):
  y = y + x
  x = 2
  y = y + x
  return y


x = 3
y = 10
y = my_function(x)
print(y)

def get_five():
 return 5
def get_and_print_five():
 five = get_five()
 print(f'Called get_five(): result is {five}')


get_and_print_five()


def get_five():
 return 5


prc_dic = {
    '3000-01-15': 7.0400,
    '2020-01-14': 7.1100,
    '2020-01-13': 7.0200,
    '2020-01-02': 7.1600,
    '2020-01-03': 7.1900,
    '2020-01-06': 7.0000,
    '2020-01-07': 7.1000,
    '2020-01-08': 6.8600,
    '2020-01-09': 6.9500,
    '2020-01-10': 7.0000,
}
prc_dic = {
    '3000-01-15': 7.0400,
    '2020-01-14': 7.1100,
    '2020-01-13': 7.0200,
    '2020-01-02': 7.1600,
    '2020-01-03': 7.1900,
    '2020-01-06': 7.0000,
    '2020-01-07': 7.1000,
    '2020-01-08': 6.8600,
    '2020-01-09': 6.9500,
    '2020-01-10': 7.0000,
}

# replace '???' with the correct expression
sorted_keys = [k for (k, v) in sorted(prc_dic.items())]
prc_dic = {('2020-01-15' if k == '3000-01-15' else k):v for k , v in prc_dic.items()}


import yfinance # (1)
tic = "QAN.AX" # (2)
start = '2020-01-01' # (3)
end = None # (4)
df = yfinance.download(tic, start, end, ignore_tz=True) # (5)
print(df) # (6)
df.to_csv('qan_stk_prc.csv') # (7)

import unicodedata
print("The copyright symbol is: \u00A9")
